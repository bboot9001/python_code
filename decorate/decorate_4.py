#/usr/bin/env python 
#-*-coding:utf-8-*-
"""以类实现的带参数的装饰器"""
class decorateWithArgument(object):
    """"""
    def __init__(self,arg1, arg2,arg3):
        print "Inside __init__()"
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self,f):
        """"""
        print "Inside __call__"
        def wrapped_f(*args):
            print "Inside wrapped_f()"
            print "Decorator arguments:", self.arg1, self.arg2,self.arg3
            f(*args)
            print "After f(*args)"
        return wrapped_f


@decorateWithArgument("Hello","world",42)
def sayHello(a1,a2,a3,a4):
    print "sayHello arguments:",  a1, a2, a3,a4


print "After decoration"

if __name__=="__main__":
    print "Preparing to call sayHello()"
    sayHello("a","d","c","d")
    print "decorate end"


