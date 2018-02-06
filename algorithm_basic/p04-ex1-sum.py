#!/usr/bin/python3

# # algorithm to get a sum of consecutive numbers (recursive)
# input: n (integer)
# output: a sum of 1~n

def sum(n):
	if n <= 1:
		return 1
	return n+sum(n-1)

print(sum(1))	
print(sum(10))	
print(sum(100))	