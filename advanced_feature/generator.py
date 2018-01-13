#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The first line is used to designate a interpreter, second line is coding
g = (x * x for x in range(10))
for n in g:
	print(n)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for n in fib(6):
	print(n)
