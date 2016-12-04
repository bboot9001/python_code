#!/usr/bin/env python
#-*-coding=utf-8-*-
import os

from functools import partial

import  hashlib

#需要安装python_magic,libmagic 的python接口
import magic 

import Image
import cropresize2
 
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
	"""
		字节大小的转换函数
	"""
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


def get_magic_mimetype(filename,mime = True):
	"""
	获取图片的类型,也可以获取文件的类型
	"""
	mimetype = magic.from_file(filename,mime)
	return mimetype

def resize_image(filename,width,height,savefilename):
	"""
		将图片按照指定的大小进行剪切
	"""
	with open(filename,'rb') as f:
		im = Image.open(f)
		img = cropresize2.crop_resize(im,(width,height))
		img.save(savefilename)




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

	print get_magic_mimetype('test.py')

	print '开始剪切文件'
	resize_image('girl.jpg',55,55,'girl55*55.jpg')
	print '剪切文件结束'

