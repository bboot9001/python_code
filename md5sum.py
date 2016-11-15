#!/usr/bin/env python
#!-*- encoding:utf-8 -*-

import hashlib 
import sys 
import os 

def md5hex(word):
	"""MD5加密算法，返回32位小写16进制符号
	"""
	if isinstance(word,unicode):
		word = word.encode("utf-8")
	elif not isinstance(word,str):
		word = str(word)
	m = hashlib.md5()
	m.update(word)
	return m.hexdigest()

def md5sum(fname):
	""" 计算文件的MD5
	"""

	def read_chunks(fh):
		fh.seek(0)
		chunk = fh.read(8096)
		while chunk:
			yield chunk
			chunk = fh.read(8096)
		else:
			fh.seek(0)
	m = hashlib.md5()
	if isinstance(fname,basestring) \
		and os.path.exists(fname):
		with open(fname,"rb") as fh:
			for chunk in read_chunks(fh):
				m.update(chunk)
	elif fname.__class__.__name__ in ["StringIO","StringO"] \
		or isinstance(fname,file):
		for chunk in read_chunks(fname):
			m.update(chunk)
	else:
		return ""
	return m.hexdigest()

if __name__ == "__main__":
	md5 = md5sum(sys.argv[1])
	fd = open(sys.argv[1],'r')
	tet = fd.read()
	mdeex = md5hex(tet)
	print md5
	print mdeex
	print "the ending"
