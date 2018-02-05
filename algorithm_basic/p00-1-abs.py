#!/bin/python3

import math

# The absolute value algorithm 1 (discriminate a sign)
# input: real number a
# output: absolute value of a

def abs_sign(a):
	if a >= 0:
		return a
	else:
		return -a

# The absolute value algorithm 2 (square number - square root)
# input: real number a
# output: absolute value of a

def abs_square(a):
	b = a*a
	return math.sqrt(b) # square root function of math module

print(abs_sign(5))
print(abs_sign(-3))
print()
print(abs_square(5))
print(abs_square(-3))
