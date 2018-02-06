#!/usr/bin/python3

# # algorithm to get a product of consecutive numbers (recursive)
# input: n (integer)
# output: a product of 1~n

def fact(n):
	if n <= 1:
		return 1
	return n*fact(n-1)

print(fact(1))	# 1!=1
print(fact(5))	# 5!=120
print(fact(10))	# 10!3628800
