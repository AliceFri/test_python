import json

import mongoengine as me
from datetime import datetime as dt


# 设置数据库连接信息 包括传入到pymongo的一些超时参数

me.connect(
    host='mongodb://127.0.0.1:27017/test',
    socketTimeoutMS=10000,
    connectTimeoutMS=3000,
    serverSelectionTimeoutMS=3000,
)


class BaseDocument(me.Document):

    """
    Base document definition.
    Defines the following attributes common to all derived models.
        :attr created_at datetime: Creation time defaulting to UTC
        :attr updated_at datetime: Updation time defaulting to UTC
    Defines the following metadata for the derived models' support.
        :attr allow_inheritance True: Required by Mongoengine.
                                        Allows inheritance
        :attr abstract True: Created derived class instances would use
                             a collection of <DerivedClass>
                              instead of BaseDocument.<DerivedClass>
    """

    created_at = me.DateTimeField(default=dt.utcnow())
    updated_at = me.DateTimeField(default=dt.utcnow())
    deleted_at = me.DateTimeField()

    meta = {
        'indexes': [],
        'sparse': True,
        'allow_inheritance': True,

        'date_str': '%d-%m-%Y'
    }

    def save(self, *args, **kwargs):
        # self.obj_id = self._get_collection().find({}).count() + 1
        super(BaseDocument, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        super(BaseDocument, self).update(*args, **kwargs)
        self.reload()

    def json(self, fields=None, excludes=None, as_string=False):

        # Pick up a list of fields for the JSON construct from the
        # fields param. If fields is not list/tuple, initialize an
        # empty list and get export fields from inherited model meta.
        # If neither is True, fetch a list of all keys from _fields
        # attribute for instance.

        # Inherited model meta declaration to get metadata for operation
        obj_meta = getattr(self, '_meta', {})

        fields = [] if not isinstance(fields, (list, tuple)) else fields
        fields.extend(obj_meta.get('export_fields', []))
        fields = fields or getattr(self, '_fields').iterkeys()


        # Pick up a list of fields for the JSON construct from the
        # excludes param. If fields is not list/tuple, initialize an
        # empty list and get exclude fields from inherited model meta.

        excludes = [] if not isinstance(
                                excludes, (list, tuple)) else excludes
        excludes = excludes or obj_meta.get('exclude_fields', []) or []


        # Dumper considerations
        # If it is a reference field, and thus has a to_mongo attr
        # do a reload before attempting a json dump of the object
        # instance. Alternatively, could consider
        # QueryObject('<Model>', {'pk':<pk>}) to update.
        # A Spec test should decide the better alternative.

        ret_val = {x: getattr(self, x).reload().json() if hasattr(
            getattr(self, x), 'to_mongo') else [
            y.reload().json() if hasattr(y, 'to_mongo') else str(y) for y
            in getattr(self, x)] if isinstance(
            getattr(self, x), me.base.datastructures.BaseList)
            else getattr(self, x) if isinstance(getattr(self, x),
            me.base.datastructures.BaseDict) else str(
            dt.strftime(getattr(self, x), obj_meta.get('date_str',
            '%d-%m-%Y'))) if isinstance(getattr(self, x), dt) else \
            str(getattr(self, x)) if getattr(self, x) else None \
            for x in fields if hasattr(self, x) and not x in excludes}

        return ret_val if not as_string else json.dumps(ret_val)


class UserDocument(BaseDocument):

    """User document definition"""

    username = me.StringField(unique=True)
    email = me.EmailField(required=True,
                            unique=True)
    metadata = me.DictField()

    meta = {
        'indexes': ['username'],
        'export_fields': ['username', 'email'],
        'exclude_fields': ['_id']
    }


class User1Document(BaseDocument):

    """User1 document definition"""

    username = me.StringField(unique=True)
    metadata = me.DictField()

    meta = {
        'indexes': ['username'],
        'export_fields': ['username', 'email'],
        'exclude_fields': ['_id']
    }


if __name__ == '__main__':
    user = UserDocument(username='test', email='aa@153.com')
    user.save()
    print(user.json())
    user1 = User1Document(username='test1')
    user1.save()
    print(user1.json())
