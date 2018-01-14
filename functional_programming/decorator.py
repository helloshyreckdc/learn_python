#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The first line is used to designate a interpreter, second line is coding
import functools
def log(text):
	def decorator(func):
	    @functools.wraps(func)
	    def wrapper(*args, **kw):
	        print('%s %s():' % (text, func.__name__))
	        return func(*args, **kw)
	    return wrapper
	return decorator

@log('execute')
def now():
	print('2018-1-14')

now()

f = now
print(now.__name__)
print(f.__name__)

