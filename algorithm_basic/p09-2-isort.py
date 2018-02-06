#!/usr/bin/python3

# Insertion sort (2)
# input: list a
# output: none(sorted list a)

def ins_sort(a):
	n = len(a)
	for i in range(1, n):
		key = a[i]
		j = i-1
		while j >= 0 and a[j] > key:
			a[j+1] = a[j]
			j-=1
		a[j+1] = key

# main

d = [2,4,5,1,3]
print("before sort d(%d)" % (len(d)))
print(d)
print("after sort")
ins_sort(d)
print(d)