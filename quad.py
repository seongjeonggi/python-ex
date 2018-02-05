#!/bin/python3

# exp. --> ax**2 + bx + c = (a!=0)
# * a discriminant --> 	D = b**2 - 4ac
# D > 0 : if has a double root,
#           x = -b(+-)sqrt(b**2-4ac) / 2a
# D = 0 : if has a single root,
#           x = -(b/2a)
# D < 0 : if no root,

import math
import sys

print("ax2 + bx + c = 0")

# input coefficients a, b, c, and convert the input string to a prime number.
a = float(input("a? "))
b = float(input("b? "))
c = float(input("c? "))

if a == 0:
	print("a=0 : not a quadratic equation.")
	sys.exit()

D = b*b-4*a*c 	# discriminate D

if D > 0:
	x1 = (-b+math.sqrt(D))/(2*a)
	x2 = (-b-math.sqrt(D))/(2*a)
	print("double root :", x1, x2)

if D == 0:
	x = -b/(2*a)
	print("single root :", x)

if D < 0:
	print("no solution.")

