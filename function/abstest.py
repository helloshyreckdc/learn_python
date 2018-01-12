#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The first line is used to designate a interpreter, second line is coding
def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand tpye')
    if x >= 0:
        return x
    else:
        return -x
