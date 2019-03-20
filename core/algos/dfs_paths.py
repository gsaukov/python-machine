graph = {'A': set(['B', 'C']),                  #     A
         'B': set(['A', 'D', 'E']),             #   /  \
         'C': set(['A', 'F']),                  #  C    B       H
         'D': set(['B']),                       #  |   / \    /  \
         'E': set(['B', 'F', 'G']),             #  |  D   E--G----I
         'F': set(['C', 'E']),                  #  |     /    \    \
         'G': set(['E', 'H', 'J', 'I']),        #   \   /      J----K
         'H': set(['G', 'I']),                  #     F
         'I': set(['H', 'G', 'K']),
         'J': set(['G', 'K']),
         'K': set(['J', 'I'])}

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def dfs_paths_rec(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths_rec(graph, next, goal, path + [next])

print(list(dfs_paths(graph, 'A', 'F')))

print(list(dfs_paths_rec(graph, 'C', 'F')))