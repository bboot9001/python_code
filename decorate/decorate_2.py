#-*-coding:utf-8-*-
"""装饰器用法理解"""
#1.简单装饰器
def use_logging(func):

    def wrapper(*args, **kwargs):
        print "before log!"
        return func(*args,**kwargs)
    return wrapper


def bar():
    print "I am a bar"

#普通装饰器
bar = use_logging(bar)

#使用语法糖
@use_logging
def foo():
    print "I am a foo"

#带参数的装饰器
def decorate_para(parameter):
    def decorate(func):
        def wrapper(*args,**kwargs):
            if parameter == "para":
                print "this is a parameter func!"
            return func(*args,**kwargs)
        return wrapper
    return decorate


@decorate_para(parameter="para")
def foo_plus(name="foo"):
    print "I am not %s" % name

#类装饰器
class ClassDecorate(object):
    def __init__(self,func):
        self.func = func
    
    def __call__(self):
        print "class decorate start"
        self.func()
        print "class decorate end"
    
@ClassDecorate
def ClassFuc():
    print "class func"


#在装饰器中保留原函数的信息
from functools import wraps
def decorate_info(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print "info remain"
        return func(*args,**kwargs)
    return wrapper

@decorate_info
def decorate_info_func():
    """函数信息"""
    print "this is info func"


        





if __name__ ==  "__main__":
    #普通装饰器
    bar()
    #语法糖装饰器
    foo()
    #带参数的装饰器
    foo_plus()
    #类装饰器
    ClassFuc()
    #保存函数的原来信息
    decorate_info_func()
    decorate_info_func.__name__
    decorate_info_func.__doc__

