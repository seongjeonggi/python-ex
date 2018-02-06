#!/usr/bin/python3

# # algorithm to get a product of consecutive numbers
# input: n (integer)
# output: a product of 1~n

def fact(n):
	f = 1
	for i in range(1, n+1):
		f=f*i
	return f

print(fact(1))	# 1!=1
print(fact(5))	# 5!=120
print(fact(10))	# 10!3628800
