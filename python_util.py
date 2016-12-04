#!/usr/bin/env python
#-*-coding=utf-8-*-
import os

from functools import partial

import  hashlib

HERE = os.path.abspath(os.path.dirname(__file__))

def get_file_md5(f,chunk_size=8192):
	"""
		计算文件的MD5,参数需要文件句柄
	"""
	h = hashlib.md5()
	while True:
		chunk = f.read(chunk_size)
		if not chunk:
			break;
		h.update(chunk)
	return h.hexdigest()


def humanize_bytes(bytesize,precision=2):
	abbrevs = (
		(1 << 50,'PB'),
		(1 << 40,'TB'),
		(1 << 30,'GB'),
		(1 << 20,'MB'),
		(1 << 10,'KB'),
		(1 , 'bytes'),
	)

	if bytesize == 1:
		return '1 byte'

	for factor, suffix in abbrevs:
		if bytesize >= factor:
			break

	return '%.*f %s' % (precision,bytesize / factor ,suffix)



get_file_path = partial(os.path.join,HERE)

if __name__ == '__main__':
	print 'start ......'
	path = get_file_path('test')
	
	print '%s' % path

	print '*'*40

	print humanize_bytes(111111,3)

	print '#'*40

	with open('md5sum.py','rb') as f:
		md5 = get_file_md5(f)
		print 'md5 is %s' % md5

