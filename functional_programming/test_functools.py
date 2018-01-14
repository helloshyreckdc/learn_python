#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The first line is used to designate a interpreter, second line is coding
import functools
int2 = functools.partial(int, base=2)
print(int2('1011'))
