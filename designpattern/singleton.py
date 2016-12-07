#!/usr/bin/env python
# encoding: utf-8

"""
    单例模式，不支持多线程模式
"""
class Singleton(type):
    _instances = {}

    def __call__(cls,*args,**kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args,**kwargs)

        return cls._instances[cls]

#python2
class MyClass(object):
    __metaclass__ = Singleton

"""单例模式方法二"""
def singleton(cls):
    instances = {}

    def wrapper(*args,**kwargs):
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)

        return instances[cls]

    return wrapper

@singleton
class Foo(object):
    pass

"""单例模式方法三"""
class Singletonex(object):
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super(Singletonex,cls).__new__(cls,*args,**kwargs)
        return cls._instance



class Fooex(Singletonex):
    pass




if __name__ == '__main__':
    a = MyClass()
    b = MyClass()

    print a == b
    print a is b

    foo1 = Foo()
    foo2 = Foo()

    print foo1 is foo2

    fooex1 = Fooex()
    fooex2 = Fooex()

    print fooex1 is fooex2





























