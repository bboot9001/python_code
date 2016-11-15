#!/usr/bin/env python
#!-*-coding:utf-8-*-
import sys
def read_in_block(filename):
	""" 使用yield读取大文件的代码片段
	"""
	BLOCK_SIZE = 8096
	with open(filename,"r") as fd:
		block = fd.read(BLOCK_SIZE)
		while block:
			yield block
			block = fd.read(BLOCK_SIZE)
#			yield block

def read_inline(filename):
	"""使用python自带的方法读取大文件
	"""
	with open(filename,"r") as fd:
		for line in fd:
			print line
			
			
if __name__ == "__main__":
	filename = sys.argv[1]
	for block in read_in_block(filename):
		print block
#	read_in_block(filename)
	print "*********开始第二个输出*********"	
#	read_inline(filename)
