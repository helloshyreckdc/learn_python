#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The first line is used to designate a interpreter, second line is coding

print('python3以Unicode编码,支持中文')
print(ord('A')) # get Unicode number of char
print(ord('中'))
print(chr(66)) # change order number into char
print(chr(25991))

print('\u4e2d\u6587')
print('ABC'.encode('ascii')) # output b'ABC', b means bytes
print('中文'.encode('utf-8'))
print(b'ABC'.decode('ascii')) 
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# next sentence would cause error
#print(b'\xe4\xb8\xad\xff'.decode('utf-8')) 
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')) 

print(len('ABC')) # compute length
print(len('中文'))

print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('shyreckdc', 1000000))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

print('Age: %s. Gender: %s' % (25, True))
print('growth rate: %d %%' % 7)
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
