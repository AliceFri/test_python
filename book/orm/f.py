import datetime
import functools
import inspect
from enum import Enum

import bson
import pydantic


def cache(fn):

    sig = inspect.signature(fn)

    default_kwargs = {}
    for k, v in sig.parameters.items():
        if v.default != inspect.Parameter.empty:
            default_kwargs[k] = v.default

    _cache = {}

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):

        kwargs = {**default_kwargs, **kwargs}

        cache_key = repr(args) + repr(sorted(kwargs.items(), key=lambda x: x[0]))

        if cache_key not in _cache:
            _cache[cache_key] = fn(*args, **kwargs)

        return _cache[cache_key]

    return wrapper


class _BaseModel(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        """
        用于支持后端发出的ObjectId转到str
        """

        json_encoders = {
            bson.ObjectId: lambda x: str(x),
            datetime.datetime: lambda x: x.isoformat()[:-3] + 'Z',
        }

    def fdict(self, exclude_unset=True, *args, **kwargs):
        """
        用于支持前端传来的ref类型的对象转换为id
        """
        def _parse(k, v):
            k: str
            self.__ref_fields__: dict[str, _BaseModel]
            if k in self.__ref_fields__:
                v = v['id'] if v else None
            if isinstance(v, Enum):
                v = v.value
            return v

        data = self.dict(exclude_unset=exclude_unset, *args, **kwargs)

        new_data = {}
        for k, v in data.items():
            if isinstance(v, list):
                v = [_parse(k, i) for i in v]
            else:
                v = _parse(k, v)
            new_data[k] = v
        return new_data

    def __iter__(self):
        """
        用于支持 * 解包
        """
        return self.fdict().__iter__()

    def keys(self):
        """
        用于支持 ** 解包
        """
        return self.fdict().keys()

    def __getitem__(self, index):
        """
        用于支持 ** 解包
        """
        return self.fdict()[index]

    def to_query(self) -> dict:
        """
        将optional_model转换为query参数
        """

        query = {}
        for k, v in self.dict().items():
            if v is None:
                continue
            if k == 'id':
                query['_id'] = v
            elif isinstance(v, Enum):
                query[k] = v.value
            elif isinstance(v, list):
                query[k] = {'$in': v}
            elif isinstance(v, str):
                query[k] = {'$regex': v}
            else:
                query[k] = v

        return query


@cache
def create_model(baseclass, include: tuple = None, exclude: tuple = None) -> _BaseModel:
    def _parse_name():
        class_name = f'{baseclass.__name__}_create_model'
        if include:
            class_name += f' include {include}'
        if exclude:
            class_name += f' exclude {exclude}'
        return class_name

    def _get_field(key, item):
        default = ... if item.required or key == 'id' else item.default
        if default == '':
            default = None

        try:    # 尝试进行递归创建model
            if issubclass(item.type_, _BaseModel):
                return (
                    create_model(
                        item.outer_type_,
                        include=sub_include.get(key),
                        exclude=sub_exclude.get(key),
                    ),
                    default,
                )
        except TypeError:
            return item.outer_type_, default
        return item.outer_type_, default

    def _parse_clude(_clude: tuple[str]):
        main = set()
        sub = {}
        if _clude:
            for _n in _clude:
                _n = _n.split('.')
                if len(_n) > 1:
                    sub.setdefault(_n[0], []).append('.'.join(_n[1:]))
                else:
                    main.add(_n[0])
        sub = {k: tuple(v) for k, v in sub.items()}
        return main, sub

    main_include, sub_include = _parse_clude(include)
    main_exclude, sub_exclude = _parse_clude(exclude)

    if main_include and main_exclude:
        raise Exception('include and exclude can not be both set')

    fields = baseclass.__fields__
    if not main_include:
        main_include = tuple(set(fields) - main_exclude)

    validators = {'__validators__': baseclass.__validators__}
    new_fields = {
        key: _get_field(key, item)
        for key, item in fields.items()
        if key in main_include or key in sub_include or key in sub_exclude
    }

    return pydantic.create_model(
        _parse_name(),
        **new_fields,
        __base__=_BaseModel,
        __validators__=validators,
        __ref_fields__=getattr(baseclass, '__ref_fields__', {}),
    )


@cache
def optional_model(baseclass) -> _BaseModel:
    fields = baseclass.__fields__
    validators = {'__validators__': baseclass.__validators__}
    new_fields = {key: (item.type_, None) for key, item in fields.items()}
    return pydantic.create_model(
        f'{baseclass.__name__}_Optional',
        **new_fields,
        __base__=_BaseModel,
        __validators__=validators,
        __ref_fields__=getattr(baseclass, '__ref_fields__', {}),
    )


def opt_create_model(baseclass, include: tuple = None, exclude: tuple = None) -> _BaseModel:
    return optional_model(create_model(baseclass, include=include, exclude=exclude))
