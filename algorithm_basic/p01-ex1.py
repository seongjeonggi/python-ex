#!/usr/bin/python3

# sum of x**2, x=[1,...,n]
# input: n
# ouput: sum of x**2, x=[1,...,n]

def sum_sq(n):		# O(n)
	s = 0
	for x in range(1, n+1):
		s = s+x**2
	return s

def sum_sq2(n):		# O(1)
	return (n*(n+1)*(2*n+1))//6

print(sum_sq(10))
print(sum_sq2(10)) 

print(sum_sq(100))
print(sum_sq2(100))