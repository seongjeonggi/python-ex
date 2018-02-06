#!/usr/bin/python3

# Quick sort (normal)
# input: list a
# output: none(sort the list)

def quick_sort_sub(a, start, end):
	if end - start <= 0:
		return

	pivot = a[end]
	i = start
	for j in range(start, end):
		if a[j] <= pivot:
			a[i], a[j] = a[j], a[i]
			i += 1

	a[i], a[end] = a[end], a[i]

	quick_sort_sub(a, start, i-1)
	quick_sort_sub(a, i+1, end)

def quick_sort(a):
	return quick_sort_sub(a, 0, len(a)-1)

# main

d = [6,8,3,9,10,1,2,4,7,5]
print("before sort d(%d)" % (len(d)))
print(d)
quick_sort(d)
print("after sort")
print(d)
