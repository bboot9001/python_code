#-*-coding:utf-8 -*-
""" 普通的装饰器"""
def outer(some_func):
    def inner():
        print "before some_func"
        ret = some_func()
        return ret + 1
    return inner

@outer
def foo():
    return 1

#foo = outer(foo)
"""更加通用的的装饰器"""
def logger(func):
    def inner(*args, **kwargs):
        print "Arguments were :%s ,%s" % (args, kwargs)
        return func(*args, **kwargs)
    return inner

@logger
def foo1(x, y):
    return x * y

@logger
def foo2():
    return 2

if __name__ == '__main__':
   # foo()
    foo1(5,4)
    foo2()
