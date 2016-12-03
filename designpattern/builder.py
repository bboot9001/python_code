#!/usr/bin/env python 
#-*-encoding:utf-8-*-

"""
建造者模式

"""

from abc import ABCMeta ,abstractmethod

class Product(object):
	"""
	"""

	def __init__(self):
		self.parts = []

	def add(self, part):
		self.parts.append(part)


	def show(self):
		print '_'.join(self.parts)



class Builder(object):
	"""
	"""

	__metaclass__ = ABCMeta

	@abstractmethod
	def build_part_1(self):
		pass

	@abstractmethod
	def build_part_2(self):
		pass

	@abstractmethod
	def get_result(self):
		pass



class BuilderA(Builder):
	def __init__(self):
		self.product = Product()

	def build_part_1(self):
		self.product.add("partA1")

	def build_part_2(self):
		self.product.add("partA2")

	def get_result(self):
		return self.product

class BuilderB(Builder):
	def __init__(self):
		self.product = Product()

	def build_part_1(self):
		self.product.add("partB1")

	def build_part_2(self):
		self.product.add("partB2")

	def get_result(self):
		return self.product

class Director(object):
	
	@staticmethod
	def construct(builder):
		builder.build_part_1()
		builder.build_part_2()

if __name__=='__main__':
	ba = BuilderA()
	bb = BuilderB()

	Director.construct(ba)
	product = ba.get_result()
	product.show()


		
	Director.construct(bb)
	product = bb.get_result()
	product.show()


