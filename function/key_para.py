#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The first line is used to designate a interpreter, second line is coding
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Bob', 35, city='Beijing')
person('Michael', 30)
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)
