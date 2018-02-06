#!/usr/bin/python3

# find duplicate name 
# input: list with 'n' in length
# output: a set of duplicate name in list

def find_same_name(a):
	n = len(a)
	result = set()
	for i in range(0, n-1):
		for j in range(i+1, n):
			if a[i] == a[j]:
				result.add(a[i])
	return result

# start

name = ["Tom", "Jerry", "Mike", "Tom"]
print(find_same_name(name))
name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(find_same_name(name2))

