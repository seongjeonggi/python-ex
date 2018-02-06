#!/usr/bin/python3

# Fibonacci sequence
# input: n (integer)
# output: n'th fibonacci number

def fibo(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	return fibo(n-1)+fibo(n-2)

print(fibo(3))
print(fibo(7))
print(fibo(31))

