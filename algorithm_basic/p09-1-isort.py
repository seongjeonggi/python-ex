#!/usr/bin/python3

# Insertion sort
# input: list a
# output: new sorted list

def find_ins_idx(r, v):
	for i in range(0, len(r)):
		if v < r[i]:
			return i

	return len(r)

def ins_sort(a):
	result=[]

	#print(a, result) # debug
	while a:
		value = a.pop(0)
		ins_idx = find_ins_idx(result, value)
		result.insert(ins_idx, value)
	#	print(value, a, result) # debug

	return result

# main

d = [2,4,5,1,3]
print("before sort d(%d)" % (len(d)))
print(d)
print("after sort")
print(ins_sort(d))