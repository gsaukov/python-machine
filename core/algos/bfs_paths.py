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

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

print(list(bfs_paths(graph, 'I', 'C')))