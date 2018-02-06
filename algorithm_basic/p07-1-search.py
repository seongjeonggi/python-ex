#!/usr/bin/python3

# Sequential search
# input: 
#		a: list
#		x: target value
# output: index of x on success, otherwise -1.

def search_list(a, x):

	n=len(a)
	for i in range(0, n):
		if x == a[i]:
			return i

	return -1

# main

v = [17,92,18,33,58,7,33,42]
print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))

