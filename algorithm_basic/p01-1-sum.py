#!/usr/bin/python3

# 1-n sum (1)
# in: n
# out: sum of numbers in 1~n

def sum_n(n):
	s = 0
	for i in range(1, n+1):
		s = s+i
	return s

print(sum_n(10))
print(sum_n(100))
