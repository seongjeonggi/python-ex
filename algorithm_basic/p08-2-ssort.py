#!/usr/bin/python3

# Selection sort (2)
# input: list a
# output: none(sorted list a)

def sel_sort(a):
	n = len(a)

	for i in range(0, n-1):
		min_idx=i
		for j in range(i, n):
			if a[j] < a[min_idx]:
				min_idx=j
		a[i], a[min_idx] = a[min_idx], a[i]

# main

d = [2,4,5,1,3]
print("before sort d(%d)" % (len(d)))
print(d)
print("after sort")
sel_sort(d)
print(d)