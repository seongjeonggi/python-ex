#!/usr/bin/python3

# Search my friends from the list
# input: g: graph of friend relationship, start: start vertex.
# output: all my friend name.

def print_all_friends(g, start):

	qu = []
	done = set()

	qu.append((start, 0))	# use tutle type => (data1, data2)

	done.add(start)

	while qu:
		(p, d) = qu.pop(0)
		print(p, d)
		for x in g[p]:
			if x not in done:
				qu.append((x, d+1))
				done.add(x)

# start main
fr_info = {
	"Summer": ["John", "Justin", "Mike"],
	"John": ["Summer", "Justin"],
	"Justin": ["John", "Summer", "Mike", "May"],
	"Mike": ["Summer", "Justin"],
	"May": ["Justin", "Kim"],
	"Kim": ["May"],
	"Tom": ["Jerry"],
	"Jerry": ["Tom"]
}

print_all_friends(fr_info, "Summer")
print()
print_all_friends(fr_info, "Jerry")