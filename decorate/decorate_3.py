#/usr/bin/env python
#-*-coding:utf-8-*-
"""装饰器带参数类实现"""

class decorateWithoutArguments(object):
    """装饰器"""
    def __init__(self,f):
        print "Inside __init__()"
        self.f = f

    def __call__(self,*args):
        """"""
        print "inside __call__()"
        self.f(*args)
        print "After self.f(*args)"


@decorateWithoutArguments
def sayHello(a1,a2,a3,a4):
    print "sayHello arguments:", a1,a2,a3,a4


print "After decoraton"
if __name__=="__main__":
    print "Preparing to call sayHello()"
    sayHello("say","hello","argument","list")
    print "After first sayHello calll"
    sayHello("a","different","set of","arguments")
    print "After second sayHello call" 
