#!/usr/bin/python3

# Quick sort (easy)
# input: list a
# output: new list(sorted)

def quick_sort(a):
	n = len(a)

	if n <= 1:
		return a

	pivot = a[-1] # expediently, select last value
	g1 = []
	g2 = []

	for i in range(0, n-1):
		if a[i] < pivot:
			g1.append(a[i])
		else:
			g2.append(a[i])

	return quick_sort(g1) + [pivot] + quick_sort(g2)

# main

d = [6,8,3,9,10,1,2,4,7,5]
print("before sort d(%d)" % (len(d)))
print(d)
print("after sort")
print(quick_sort(d))
