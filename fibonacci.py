#!/usr/bin/env python
#!-*-coding:utf-8-*-

class Fab(object):
	"""计算斐波那契数列的前n个数
	"""
	def __init__(self,max):
		self.max = max
		self.n ,self.a,self.b = 0,0,1

	def __iter__(self):
		return self


	def next(self):
		if self.n < self.max:
			r = self.b
			self.a , self.b = self.b,self.a + self.b
			self.n += 1
			return r 
		raise StopIteration()


if __name__ == "__main__":
	fab = Fab(10)
	for index in fab:
		print index
