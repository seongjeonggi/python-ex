#!/usr/bin/python3

# Get all possible combination to make pairs among n people.
# input: list with 'n' in length
# output: all sets of pairs

def make_pair(a):
	n = len(a)
	result = set()
	for i in range(0, n-1):
		for j in range(i+1, n):
			if a[i] != a[j]:
				result.add(str(a[i]+"-"+a[j]))
				
	return result

# start

name = ["Tom", "Jerry", "Mike", "Tom"]
print(make_pair(name))
name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(make_pair(name2))
name3 = ["Tom", "Jerry", "Mike"]
print(make_pair(name3))


