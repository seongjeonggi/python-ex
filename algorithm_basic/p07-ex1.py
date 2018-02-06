#!/usr/bin/python3

# Sequential search (2)
# input: 
#		a: list
#		x: target value
# output: all index of x on success, otherwise -1.

def search_list(a, x):

	n=len(a)
	xl = list()
	for i in range(0, n):
		if x == a[i]:
			xl.append(i)

	return xl

# main

v = [17,92,18,33,58,7,33,42]
print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))

