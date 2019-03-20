from random import randint
row_num = 10
col_num = 10

list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        if randint(0,10) % 7 == 0:
            list[row][col] = 'X'
        else:
            list[row][col] = 0

list[randint(0,row_num)][randint(0,col_num)] = 'G'

print(str(list).replace('], [',']\n[').replace(', ', '\t'), '\n')

def play(list, pos_x, pos_y, last_move):
    if(found(list, pos_x, pos_y)):
        return print('I have found')
    if(blocked(list, pos_x, pos_y)):
        return print('I m done')

def canmoveleft(list, pos_x, pos_y):
    new_pos_x = pos_x - 1
    if new_pos_x > 0 and canmove(list, new_pos_x, pos_y):
        return True

def canmoveup(list, pos_x, pos_y):
    new_pos_y = pos_y - 1
    if new_pos_y > 0 and canmove(list, pos_x, new_pos_y):
        return True

def canmoveright(list, pos_x, pos_y):
    new_pos_x = pos_x + 1
    if canmove(list, new_pos_x, pos_y):
        return True

def canmovedown(list, pos_x, pos_y):
    new_pos_y = pos_y + 1
    if canmove(list, pos_x, new_pos_y):
        return True

def canmove(list, pos_x, pos_y):
    return list[pos_x][pos_y] == 0 or list[pos_x][pos_y] == 'G'

def blocked(list, pos_x, pos_y):
    return canmoveleft(list, pos_x, pos_y) or canmoveup(list, pos_x, pos_y) or canmoveright(list, pos_x, pos_y) or canmovedown(list, pos_x, pos_y)

def found(list, pos_x, pos_y):
    return list[pos_x][pos_y] == 'G'


def getmoves(list, prev_moves):
    new_moves = [[]]
    for move in prev_moves:
        if canmoveup(list, move[0], move[1]):
            new_moves.insert(2,4)