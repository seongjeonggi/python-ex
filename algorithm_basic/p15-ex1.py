#!/usr/bin/python3

# Binary tree(Graph) traverse
# input: g: graph of friend relationship, start: start vertex.
# output: all vertexes.

def print_all_nodes(g, start):

	qu = []
	done = set()

	qu.append(start)

	done.add(start)

	while qu:
		p = qu.pop(0)
		print(p)
		for x in g[p]:
			if x not in done:
				qu.append(x)
				done.add(x)

# start main
G = {
	"1": ["2", "3"],
	"2": ["1", "4", "5"],
	"3": ["1"],
	"4": ["2"],
	"5": ["2"]
}

print_all_nodes(G, "1")
print()
print_all_nodes(G, "5")