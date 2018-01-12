#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The first line is used to designate a interpreter, second line is coding
# dict, list could not be a key for it's alterable
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])
d['Adam'] = 67
print(d)
print('dc' in d)
d.get('Adam')  # if not found, return none
d.get('dc', -1) # if not found, return -1
d.pop('Bob')
print(d)

# set
s = set([1, 2, 3])
s.add(4)
s.remove(2)

s1 = set([2, 3, 4])
s2 = set([1, 2, 3])
print(s1 & s2)
print(s1 | s2)

a = ['c', 'b', 'a']
a.sort()
print(a)

a = 'abc'
a.replace('a', 'A')
print(a)

