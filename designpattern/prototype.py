#!/usr/bin/env python
# encoding: utf-8
"""
原型模式
"""
import copy
from abc import ABCMeta ,abstractmethod

class Prototype(object):
    """
    原型模式
    """
    __metaclass__ = ABCMeta

    def __init__(self,id):
        self.__id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,value):
        self.__id = value

    @abstractmethod
    def clone(self):
        pass


class ConcretePrototypeA(Prototype):
    """
    具体原型类，实现一个克隆自身的操作
    """
    def clone(self):
        #浅拷贝
        return copy.copy(self)


class ConcretePrototypeB(Prototype):
    """
    具体原型类 实现一个克隆自身的操作
    """
    def clone(self):
        return copy.copy(self)


if __name__ == '__main__':
    ca = ConcretePrototypeA(1)
    c2 = ca.clone()

    print c2.id





