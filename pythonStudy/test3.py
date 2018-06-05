# -*- coding: utf-8 -*-

import functools
import time
import datetime

def log(obj):
	if type(obj).__name__ == 'function':
		@functools.wraps(obj)
		def wrapper(*args, **kw):
			print('call %s():' % obj.__name__)
			return obj(*args, **kw)
		return wrapper
	else: 
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args, **kw):
				print('%s %s():' % (obj, func.__name__))
				return func(*args, **kw)
			return wrapper
		return decorator
	
def log2(*largs):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s():' % (func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log
def now():
    print('2015-3-25')


def metric(fn):
	def wrapper(*args, **kw):
		begin = time.time()
		L = fn(*args, **kw)
		end = time.time()
		print(fn.__name__, 'excute time', end-begin)
		return L
	return wrapper
	
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
	
	
	
	
	
	
	
	
	
	
	