# -*- coding: utf8 -*-


"""
# BFS 代码模板

def BFS(graph, start, end):

	queue = []
	queue.append([start])
	visited.add(start)

	while queue:
		node = queue.pop(0)
		visited.add(node)

		process(node)
		nodes = generate_related_nodes(node)
		queue.append(nodes)
    # other processing work
    ...


#DFS 递归写法
def dfs(node, visited):
    if node in visited: # terminator
	    # already visited
	    return

	visited.add(node)

	# process current node here.
	...
	for next_node in node.children():
		if next_node not in visited:
			dfs(next_node, visited)


#DFS 非递归写法

def DFS(self, tree):

	if tree.root is None:
		return []

	visited, stack = [], [tree.root]

	while stack:
		node = stack.pop()
		visited.add(node)

		process (node)
		nodes = generate_related_nodes(node)
		stack.append(nodes)

	# other processing work
	...
"""

aaa = [1,2,3]
