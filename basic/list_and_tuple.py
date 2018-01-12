#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The first line is used to designate a interpreter, second line is coding
# List
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
len(classmates)
print(classmates[0])
print(classmates[-1])
classmates.append('Adam')
classmates.insert(1, 'Jack')
print(classmates)
classmates.pop()
print(classmates)
classmates[1] = 'dc'
print(classmates)

s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))
print(s[2][1])

# Tuple
classmates = ('Michael', 'Bob', 'Tracy')
t = (1, 2)
t = (1,)  # If there's only one element, comma is needed
# tuple is immutable, but list is alterable
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'x'
t[2][1] = 'y'
print(t)
