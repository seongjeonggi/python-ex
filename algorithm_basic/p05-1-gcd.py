#!/usr/bin/python3

# Get a GCD(Greatest Common Divisor)
# input: a, b (both integer)
# output: gcd of a and b

def gcd(a, b):
	i = min(a, b)
	while True:
		if a%i == 0 and b % i ==0:
			return i
		i = i-1

print(gcd(1,5))
print(gcd(3,6))
print(gcd(60,24))
print(gcd(81,27))
print(gcd(17,13))

