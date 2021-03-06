#!/usr/bin/env python 
#-*-coding:utf-8-*-

"""
桥接模式
将抽象部分与他的实现部分分离，使他们可以独立的变化

"""

from abc import ABCMeta , abstractmethod

class Implementor(object):
	__metaclass__ = ABCMeta 

	
	@abstractmethod
	def operation(self):
		pass

class ConcreteImplementorA(Implementor):
	def operation(self):
		print "plan A"


class ConcreteImplementorB(Implementor):
	def operation(self):
		print "plan B"

class Abstraction(object):
	def __init__(self,implementor=None):
		if implementor is not None:
			self.__implementor = implementor

	@property
	def implementor(self):
		return self.__implementor

	@implementor.setter
	def implementor(self,value):
		self.__implementor = value

	def operation(self):
		self.__implementor.operation()

class RefinedAbstraction(Abstraction):
	pass

if __name__ == '__main__':
	ab = RefinedAbstraction()
	ab.implementor = ConcreteImplementorA()
	ab.operation()

	ab.implementor = ConcreteImplementorB()
	ab.operation()

