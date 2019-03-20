

def mine_sweeper(walls, row_num, col_num):
    list = [[0 for col in range(col_num)] for row in range(row_num)]
    for wall in walls:
        list[wall[0]][wall[1]] = '#'

    list[7][7] = 'X'
    visited = []
    visited.append((0, 0))
    availible = lookAround([], visited, list, visited[0])
    paths = {}
    for x in scan(list, availible, visited, paths):
        print('========================================')
        print(str(list).replace('],', ']\n'))
    return list

def scan(list, availible, visited, paths):
    while availible:
        field = availible.pop(0)
        pos_y = field[0]
        pos_x = field[1]

        if list[pos_y][pos_x] == 'X':
            print('found ', pos_y, pos_x, paths[visited[-1]])
            return list
        else:
            buildPath(visited, paths, field)
            visited.append((pos_y, pos_x))
            yield availible.extend(lookAround(availible, visited, list, field))


def lookAround(availible, visited, list, field):
    pos_y = field[0]
    pos_x = field[1]

    up    = findMoves(availible, visited, list, pos_y-1, pos_x  )
    left  = findMoves(availible, visited, list, pos_y,   pos_x+1)
    down  = findMoves(availible, visited, list, pos_y+1, pos_x  )
    right = findMoves(availible, visited, list, pos_y,   pos_x-1)

    return appendAll(up, left, down, right)


def findMoves(availible, visited, list, pos_y, pos_x):
    if pos_y < 0:
        return None
    if pos_x < 0:
        return None
    if len(list[0]) <= pos_x:
        return None
    if len(list) <= pos_y:
        return None
    if (pos_y, pos_x) in visited:
        return None
    if (pos_y, pos_x) in availible:
        return None
    if list[pos_y][pos_x] == '#':
        return None
    return pos_y, pos_x

def appendAll(*args):
    res = []
    for arg in args:
        res.append(arg) if arg is not None else None
    return res

def buildPath(visited, paths, field):
    prev_field = visited[-1]
    if paths.get(prev_field) is None:
        paths[field] = [field]
    else:
        path = paths.get(prev_field) + [field]
        paths[field] = path
        del paths[prev_field]




print(str(mine_sweeper([[1, 2], [1, 3], [8, 3], [7, 4], [6, 2], [6, 3], [9, 9]], 10, 10)).replace('],', ']\n'))


