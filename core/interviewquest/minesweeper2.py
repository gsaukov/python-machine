

def mine_sweeper(bombs, num_rows, num_cols):
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]

    for bomb_location in bombs:
        (bomb_row, bomb_col) = bomb_location
        field[bomb_row][bomb_col] = -1

        row_range = range(bomb_row - 1, bomb_row + 2)
        col_range = range(bomb_col - 1, bomb_col + 2)

        for i in row_range:
            for j in col_range:
                if(0 <= i < num_rows and 0 <= j < num_cols and field[i][j] != -1):
                    field[i][j] += 1

    return field


print(str(mine_sweeper([[1, 2], [1, 3], [8, 3], [7, 4], [6, 2], [6, 3], [9, 9]], 10, 10)).replace('],', ']\n'))


