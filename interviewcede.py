#!/usr/bin/env python
#-*- coding:utf-8 -*-
class A(object):
    """
    生成器变量的作用域问题gen1为错误的写法，gen为改正后的写法
    """
    x = 1
    gen = (lambda x: ( x for _  in xrange(10)))(x)
    gen1 =  (x for _ in xrange(11))


if __name__ == "__main__":
   print(list(A.gen))
#    print(list(A.gen1))
