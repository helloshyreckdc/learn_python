#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The first line is used to designate a interpreter, second line is coding
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print(key)
for k, v in d.items():
	print(k, v)


from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)
