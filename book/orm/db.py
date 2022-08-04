import pymongo

_CLIENT = None
_DB = None

__all__ = [
    'register_collection',
    'get_db',
    'get_client',
    'get_collection',
]


def register_collection(client_uri, db_name):
    global _DB, _CLIENT
    _CLIENT = pymongo.MongoClient(client_uri)
    _DB = _CLIENT[db_name]


def get_db():
    if _DB is None:
        raise Exception('DB not registered')
    return _DB


def get_client():
    if _CLIENT is None:
        raise Exception('Client not registered')
    return _CLIENT


def get_collection(collection_name):
    return get_db()[collection_name]
