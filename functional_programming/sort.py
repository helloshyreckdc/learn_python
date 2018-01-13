#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The first line is used to designate a interpreter, second line is coding
print(sorted([36, 5, -12, 9, -21]))

# key could receive diffent func
print(sorted([36, 5, -12, 9, -21], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

# reverse order
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0]
L2 = sorted(L, key=by_name)
print(L2)
