import time
from datetime import timedelta

from mongoengine import StringField

from mongo import *


class BaseUpdateInfo:
    created_at = me.DateTimeField(default=dt.utcnow())
    updated_at = me.DateTimeField(default=dt.utcnow())
    deleted_at = me.DateTimeField()


class BaseDocument(me.Document):
    meta = {
        'abstract': True,
    }
    created_at = me.DateTimeField(default=dt.utcnow())
    updated_at = me.DateTimeField(default=dt.utcnow())


class BaseDocument1(me.Document):
    meta = {
        'abstract': True,
    }
    deleted_at = me.DateTimeField()


class T1(BaseDocument):
    s1 = StringField(required=True)

    def __str__(self):
        print()
        return f'{self.created_at}, {self.updated_at}, {self.deleted_at}, {self.s1}'


class T2(BaseDocument, BaseDocument1):
    s2 = StringField(required=True)


if __name__ == '__main__':
    t1 = T1(s1='s1')
    t1.save()
    t2 = T2(s2='s2')
    t2.updated_at = t1.updated_at + timedelta(days=1)
    t2.deleted_at = t1.updated_at + timedelta(days=1)
    t2.save()
    print(t1.updated_at, t2.updated_at)
    #
    # b1 = BaseDocument()
    # b1.save()