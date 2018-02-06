#!/usr/bin/python3

# Euclid's GCD(Greatest Common Divisor) algorithm
# input: a, b (both integer)
# output: gcd of a and b

def gcd(a, b):
	if b==0:
		return a
	return gcd(b, a%b)

print(gcd(1,5))
print(gcd(3,6))
print(gcd(60,24))
print(gcd(81,27))
print(gcd(17,13))

