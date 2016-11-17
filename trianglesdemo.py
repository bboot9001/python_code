#!/usr/bin/env python
#!-*-coding:utf-8-*-

def triangles(max):
	n = 0
	a=[1]
	while n < max :
		yield a 
		a = [sum(i) for i in zip([0] + a,a + [0])]
		n+=1


if __name__ == "__main__":
	for x in triangles(6):
		print(x)
