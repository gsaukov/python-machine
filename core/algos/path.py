graph = {'A': set(['B', 'C']),                  #     A
         'B': set(['A', 'D', 'E']),             #   /  \
         'C': set(['A', 'F']),                  #  C    B       H
         'D': set(['B']),                       #  |   / \    /  \
         'E': set(['B', 'F', 'G']),             #  |  D   E--G----I
         'F': set(['C', 'E', 'F1']),            #  |     /    \    \
         'G': set(['E', 'H', 'J', 'I']),        #   \   /      J----K
         'H': set(['G', 'I']),                  #     F---F1
         'I': set(['H', 'G', 'K']),             #          \
         'J': set(['G', 'K']),                  #           F2
         'K': set(['J', 'I']),
         'F1': set(['F', 'F2']),
         'F2': set(['F', 'F1']),
         }


def dfs_paths_rec(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths_rec(graph, next, goal, path + [next])

print(list(dfs_paths_rec(graph, 'I', 'F2')))