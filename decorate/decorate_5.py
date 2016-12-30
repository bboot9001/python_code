#/usr/bin/env python
#-*-coding:utf-8-*-
"""以函数实现带参数的装饰器 """
def decorateWithArguments(*outerargs):
    def decorate(func):
        def wrapper(*args,**kwargs):
            print "FuncDecorate start :", outerargs
            func(*args,**kwargs)
            print("FuncDecorate end")
        return wrapper
    return decorate

@decorateWithArguments("dhfakh")
def funcdec(*args,**kwargs):
    print "this is :" , args,kwargs


if __name__=="__main__":
    funcdec((1,2,4),{'w':123,'p':456})

