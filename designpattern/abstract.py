#/usr/bin/env python 
#-*-coding:utf-8-*-
"""
模板方法模式

"""
from abc import ABCMeta, abstractmethod

class AbstractClass(object):
	"""
	实现一个模板方法
	"""
	__metaclass__ = ABCMeta

	def say_hello(self):
		print "begin..."
		self.hello()
		self.world()
		print "end..."

	@abstractmethod
	def hello(self):
		pass

	@abstractmethod
	def world(self):
		pass


class ConcreteClass(AbstractClass):
	"""
	实现了特定的步骤
	"""

	def hello(self):
		print "hello"


	def world(self):
		print "world"

if __name__ == '__main__':
	c = ConcreteClass()
	c.say_hello()
