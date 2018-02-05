#!/usr/bin/python3

# 1-n sum (2)
# in: n
# out: sum of numbers in 1~n

def sum_n(n):
	return n*(n+1)//2

print(sum_n(10))
print(sum_n(100))
