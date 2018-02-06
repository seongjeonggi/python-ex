#!/usr/bin/python3

# Bubble sort 
# input: list a
# output: none(sort the list)

def bubble_sort(a):
	n = len(a)

	b=True
	while b:
		b=False
		for i in range(0, n-1):
			if a[i] > a[i+1]:
				a[i], a[i+1] = a[i+1], a[i]
				b=True

# main

import sys
import random as r

if len(sys.argv) != 2:
	print("usage: $ py %s <list size>" % sys.argv[0])
	sys.exit()
n = int(sys.argv[1])

d = []
for i in range(0, n):
	d.append(r.randint(1, n))

# d = [6,8,3,9,10,1,2,4,7,5]
print("before sort d(%d)" % (len(d)))
print(d)
bubble_sort(d)
print("after sort")
print(d)
