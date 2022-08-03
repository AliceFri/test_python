# 单例模式

# 1. 模块， 全局变量
# 2. 装饰器
# 3. 元类, metaclass  type.__call__ -> __new__ -> __init__

# 饱汉 饿汉
# 多线程 加锁， 二次确认(避免加锁)

def singleton(cls):
    _Singleton = {}

    def inner(*args, **kwargs):
        if cls not in _Singleton:
            _Singleton[cls] = cls(*args, **kwargs)
        return _Singleton[cls]
    return inner


@singleton
class Cls(object):

    def __init__(self, a):
        self.m_A = a


class MetaSingleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        print("__call__")
        obj = super(MetaSingleton, cls).__call__(*args, **kwargs)
        print(obj)
        print("__call__ 2")
        return obj


class NewSingleton(metaclass=MetaSingleton):
    _Singleton = None

    def __new__(cls, *args, **kwargs):
        print('__new__')
        if not cls._Singleton:
            cls._Singleton = object.__new__(cls)
        print(cls._Singleton)
        return cls._Singleton

    def __init__(self, a):
        print('__init__')
        self.m_A = a


if __name__ == '__main__':
    print(Cls)
    cls1 = Cls(1)
    cls2 = Cls(2)
    print(id(cls1), id(cls2), cls2.m_A, cls1.m_A)

    n1 = NewSingleton(1)
    n2 = NewSingleton(2)
    print(id(n1), id(n2), n1.m_A, n2.m_A)

