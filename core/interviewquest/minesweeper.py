

def mine_sweeper(mines, row_num, col_num):
    list = [[0 for col in range(col_num)] for row in range(row_num)]
    for mine in mines:
        list[mine[0]][mine[1]] = -1

    for row in range(row_num):
        for col in range(col_num):
            if list[row][col] == -1:
                #i am mine
                pass
            else:
                list[row][col] = lookAround(list, row, col)
    return list

def lookAround(list, pos_y, pos_x):
    return findMine(list, pos_y-1, pos_x  ) + \
           findMine(list, pos_y-1, pos_x+1) + \
           findMine(list, pos_y,   pos_x+1) + \
           findMine(list, pos_y+1, pos_x+1) + \
           findMine(list, pos_y+1, pos_x  ) + \
           findMine(list, pos_y+1, pos_x-1) + \
           findMine(list, pos_y,   pos_x-1) + \
           findMine(list, pos_y-1, pos_x-1)


def findMine(list, pos_y, pos_x):
    if pos_y < 0:
        return 0
    if pos_x < 0:
        return 0
    if len(list[0]) <= pos_x:
        return 0
    if len(list) <= pos_y:
        return 0
    if list[pos_y][pos_x] == -1:
        return 1

    return 0

print(str(mine_sweeper([[1, 2], [1, 3], [8, 3], [7, 4], [6, 2], [6, 3], [9, 9]], 10, 10)).replace('],', ']\n'))


