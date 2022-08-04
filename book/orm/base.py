from enum import Enum
from typing import List, Dict, Any, Tuple, Union

import bson
import pydantic
import pymongo

from .db import get_collection
from .const import *
from .f import _BaseModel


class ObjectId(bson.ObjectId):
    @classmethod
    def __get_validators__(cls):  # type: ignore
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema: Dict) -> None:
        field_schema.update(
            examples=["5f85f36d6dfecacc68428a46", "ffffffffffffffffffffffff"],
            example="5f85f36d6dfecacc68428a46",
            type="string",
        )

    @classmethod
    def validate(cls, v: Any) -> bson.ObjectId:
        if isinstance(v, (bson.ObjectId, cls)):
            return v
        if isinstance(v, str) and bson.ObjectId.is_valid(v):
            return bson.ObjectId(v)
        raise TypeError("invalid ObjectId specified")


class BaseModelMetaclass(pydantic.main.ModelMetaclass):
    def __new__(mcs, name, bases, namespace, **attrs):
        # 添加主键id, 暫不支持自定义
        if (
            namespace.get('__annotations__')
            and 'id' not in namespace['__annotations__']
        ):
            namespace['__annotations__']['id'] = ObjectId
            namespace['id'] = None

        cls = super().__new__(mcs, name, bases, namespace, **attrs)
        # 保存引用信息
        cls.__ref_fields__ = {}
        for name, annotation_cls in cls.__annotations__.items():
            try:
                if issubclass(annotation_cls, BaseModel):
                    cls.__ref_fields__[name] = annotation_cls
            except TypeError:
                pass

        # 创建索引
        for index in getattr(cls.Config, '_indexs', []):
            cls.get_collection().create_index(index[0], **index[1])

        # 保存delete_rule
        for ref_cls, field, rule in getattr(cls.Config, '_delete_rule', []):
            ref_cls.register_delete_rule(cls, field, rule)

        return cls


class BaseModel(_BaseModel, metaclass=BaseModelMetaclass):

    @classmethod
    def get_collection_name(cls) -> str:
        if '_collection_name' not in cls.__dict__:
            cls._collection_name = (
                "".join("_%s" % c if c.isupper() else c for c in cls.__name__)
                .strip("_")
                .lower()
            )
        return cls._collection_name

    @classmethod
    def get_collection(cls) -> pymongo.collection.Collection:
        return get_collection(cls.get_collection_name())

    @classmethod
    def get_ref(cls) -> Dict[str, 'BaseModel']:
        return getattr(cls, '__ref_fields__', {})

    @classmethod
    def get_delete_rule(cls) -> Dict[Tuple[type, str], int]:
        return getattr(cls, '_delete_rule', {})

    @classmethod
    def aggregate(cls, pipeline: List[dict]) -> List[dict]:
        page = list(cls.get_collection().aggregate(pipeline))
        return page

    @classmethod
    def objects(cls, **query) -> List[Dict[str, Any]]:
        if 'id' in query:
            query['_id'] = query.pop('id')
        return list(cls.get_collection().find(query))

    @classmethod
    def insert_one(cls, **doc):
        doc = cls.mdict(doc)
        return cls.get_collection().insert_one(doc)

    @classmethod
    def insert_many(cls, doc_list: List[Dict[str, Any]]):
        doc = [cls.mdict(d) for d in doc_list]
        return cls.get_collection().insert_many(doc)

    @classmethod
    def create_index(cls, keys, **kwargs):
        cls.get_collection().create_index(keys, **kwargs)

    @classmethod
    def parse_obj(cls, doc: Dict[str, Any]) -> Union['BaseModel', None]:
        if not doc:
            return None
        d = {}
        for k, v in doc.items():
            if v is None:
                continue
            elif k in cls.get_ref():
                d[k] = cls.get_ref()[k].parse_obj(v)
            else:
                d[k] = v
        return cls(**d)

    @classmethod
    def _cascade_find_pipeline(cls) -> List[dict]:
        pipeline = []
        for name, ref_cls in cls.get_ref().items():
            pipeline.extend(
                [
                    {
                        "$lookup": {
                            "from": ref_cls.get_collection_name(),
                            "localField": name,
                            "foreignField": "_id",
                            "as": name,
                            "pipeline": [
                                *BASE_PIPELINE,
                                *ref_cls._cascade_find_pipeline(),
                            ],
                        }
                    },
                    {
                        '$set': {
                            name: {'$arrayElemAt': [f'${name}', 0]},
                        },
                    },
                ]
            )
        return pipeline

    @classmethod
    def find_one(cls, sort=None, **query) -> Union['BaseModel', None]:
        """
        查询一条记录
        """

        result = cls.find(sort=sort, limit=1, **query)
        if not result:
            return None
        return result[0]

    @classmethod
    def find(cls, sort=None, limit=None, after_query=None, **query) -> List['BaseModel']:
        pipeline = BASE_PIPELINE.copy()
        if query:
            pipeline.append({"$match": query})
        if sort:
            pipeline.append({"$sort": sort})
        if limit and limit > 0:
            pipeline.append({"$limit": limit})
        pipeline.extend(cls._cascade_find_pipeline())
        if after_query:
            pipeline.append({"$match": after_query})
        return [cls.parse_obj(doc) for doc in cls.aggregate(pipeline)]

    @classmethod
    def register_delete_rule(cls, ref_cls, field, rule):
        delete_rule = getattr(cls, '_delete_rule', {})
        delete_rule[(ref_cls, field)] = rule
        cls._delete_rule = delete_rule

    @classmethod
    def mdict(cls, input_dict):
        """
        将字典转换为mongodb的字典格式
        """

        d = {}
        for k, v in input_dict.items():
            if k is None:
                continue
            if k in cls.get_ref() and isinstance(v, BaseModel) and v._is_exist():
                # 引用类型存在, 转成OID，如果传进来的就是OID，则不做处理
                d[k] = v.id
            elif isinstance(v, Enum):
                d[k] = v.value
            else:
                d[k] = v
        return d

    def _is_exist(self) -> bool:
        """
        检查数据库中是否存在ID相同的记录
        """
        if self.id and self.get_collection().find_one({"_id": self.id}):
            return True
        return False

    def doc(self) -> Dict[str, Any]:
        """
        转换为mongodb的字典格式
        """

        return self.mdict(self.__dict__)

    def save(self):
        if self._is_exist():
            self.update()
            return
        doc = self.doc()
        doc.pop('id', None)
        res = self.get_collection().insert_one(doc)
        self.id = res.inserted_id

    def delete(self):
        if not self._is_exist():
            raise Exception("is not exist")

        self.get_collection().delete_one({'_id': self.id})
        # ref_delete
        for (ref_cls, field), rule in self.get_delete_rule().items():
            if rule == DELETE_RULE_SET_NULL:
                ref_cls.get_collection().update_many(
                    {field: self.id},
                    {'$set': {field: None}},
                )
            elif rule == DELETE_RULE_CASCADE:
                ref_cls.get_collection().delete_many({field: self.id})

    def update(self, **update_dict):  # 传入参数暂不支持更新引用类型
        if not self._is_exist():
            raise Exception("is not exist")

        if not update_dict:
            update_dict = self.doc()
        else:
            update_dict = self.mdict(update_dict)
        update_dict.pop('id', None)
        self.get_collection().update_one({'_id': self.id}, {'$set': update_dict})
