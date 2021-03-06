#!/usr/bin/python3

# Merge sort (normal) descend
# input: list a
# output: none(sorted list)

def merge_sort(a):
	n = len(a)

	if n <= 1:
		return

	mid = n//2
	g1 = a[:mid]
	g2 = a[mid:]
	merge_sort(g1)
	merge_sort(g2)

	i1 = 0
	i2 = 0
	ia = 0

	while i1 < len(g1) and i2 < len(g2):
		if g1[i1] > g2[i2]:
			a[ia] = g1[i1]
			i1 += 1
			ia += 1
		else:
			a[ia] = g2[i2]
			i2 += 1
			ia += 1

	while i1 < len(g1):
		a[ia] = g1[i1]
		i1 += 1
		ia += 1

	while i2 < len(g2):
		a[ia] = g2[i2]
		i2 += 1
		ia += 1

# main

d = [6,8,3,9,10,1,2,4,7,5]
print("before sort d(%d)" % (len(d)))
print(d)
print("after sort")
merge_sort(d)
print(d)
