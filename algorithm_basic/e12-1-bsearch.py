#!/usr/bin/python3

# Binary search (recursive)
# input: list a, target x
# output: target position on success, otherwise -1

def binary_search_sub(a, x, start, end):
	
	if start > end:
		return -1

	mid = (start+end) // 2 

	if x==a[mid]:
		return mid
	elif x > a[mid]:
		return binary_search_sub(a, x, mid+1, end)
	else:
		return binary_search_sub(a, x, start, mid-1)

def binary_search(a, x):
	return binary_search_sub(a, x, 0, len(a)-1)

# main

import sys
import random as r

if len(sys.argv) != 2:
	print("usage: $ python3 %s <list size>" % sys.argv[0])
	sys.exit()
n = int(sys.argv[1])

d = []
for i in range(0, n):
	d.append(r.randint(1, 100))

d.sort()
print(d)
x=r.choice(d)
print(x, "=>", binary_search(d, x))

'''
d = [1,4,9,16,25,36,49,64,81]
print(binary_search(d, 0, len(d)-1, 36))
print(binary_search(d, 0, len(d)-1, 50))
'''

