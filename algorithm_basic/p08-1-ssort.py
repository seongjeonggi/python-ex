#!/usr/bin/python3

# Selection sort
# input: list a
# output: sorted list


def find_min_idx(a):
	n = len(a)
	min_idx = 0

	for i in range(1, n):
		if a[i] < a[min_idx]:
			min_idx = i

	return min_idx

def sel_sort(a):
	result = []
	while a:
		min_idx = find_min_idx(a)
		value = a.pop(min_idx)
		result.append(value)

	return result

# main

d = [2,4,5,1,3]
print("before sort d(%d)" % (len(d)))
print(d)
print("after sort")
print(sel_sort(d))