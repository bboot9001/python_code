#!/usr/bin/env python
# encoding: utf-8

"""示例1: 最简单的函数，表示调用了两次"""

def myfunc():
    print "myfunc() called."

""" 示例二 使用函数在函数的执行前后分别附加额外功能"""

def deco(func):
    print "before myfunc2 called."
    func()
    print "after myfunc2 called."
    return func

def myfunc2():
    print "myfunc2 called."

#myfunc2 = deco(myfunc2)

@deco
def myfunc3():
    print "myfunc3 called."


if __name__ == '__main__':
#    myfunc()
#    myfunc()
#    myfunc2()
#    myfunc2()
    myfunc3()
    myfunc3()