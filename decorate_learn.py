#!/usr/bin/env python
# encoding: utf-8

"""示例1: 最简单的函数，表示调用了两次"""

def myfunc():
    print "myfunc() called."

""" 示例二 使用函数在函数的执行前后分别附加额外功能"""

def deco(func):
    print "before myfunc called."
    func()
    print "after myfunc called."
    return func

def myfunc2():
    print "myfunc called."

myfunc2 = deco(myfunc2)

if __name__ == '__main__':
#    myfunc()
#    myfunc()
     myfunc2()
     myfunc2()