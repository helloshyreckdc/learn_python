#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The first line is used to designate a interpreter, second line is coding
def cal(*numbers):  # add a * to denote variable para
	sum = 0
	for number in numbers:
		sum += number * number
	return sum

print(cal(1, 2))
print(cal())
print(cal(1))
s = [1, 2, 3]
print(cal(*s))  # add a * to change list into variable para
