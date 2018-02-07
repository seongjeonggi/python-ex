#!/usr/bin/python3

# Find the same name
# input: list a with n in length, string type
# output: a set of the duplicate names from the list

def find_same_name(a):
	# Step 1: Create a dictionary with the appeared names.
	name_dict = {}
	for name in a:
		if name in name_dict:
			name_dict[name] += 1
		else:
			name_dict[name] = 1

	# Step 2: Add to 'result' that the number of times 2 or more.
	result = set()
	for name in name_dict:
		if name_dict[name] >= 2:
			result.add(name)

	return result

name = ["Tom", "Jerry", "Mike", "Tom"]
print(find_same_name(name))

name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(find_same_name(name2))