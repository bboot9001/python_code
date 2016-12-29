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

bar = use_logging(bar)

bar()