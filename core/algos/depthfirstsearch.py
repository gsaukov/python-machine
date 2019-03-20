graph = {'A': set(['B', 'C']),                  #     A
         'B': set(['A', 'D', 'E']),             #   /  \
         'C': set(['A', 'F']),                  #  C    B
         'D': set(['B']),                       #  |   / \
         'E': set(['B', 'F']),                  #  |  D   E
         'F': set(['C', 'E'])}                  #  |     /
                                                #   \   /
                                                #     F

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)

    return visited

def dfsrec(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfsrec(graph, next, visited)
    return visited

dfs(graph, 'A')

dfsrec(graph, 'C')
