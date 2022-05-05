#шебанг, ввод матрицы

def max_coins(rows, cols, coins, curr_row, curr_col):
    if curr_row == rows - 1:
        if curr_col == cols - 1:
            return coins[rows - 1][cols - 1]
        elif curr_row < rows - 1:
            return coins[curr_row][curr_col] + max_coins(rows, cols, coins, curr_row, curr_col + 1)
    elif curr_row < rows - 1:
        if curr_col == cols - 1:
            return coins[curr_row][curr_col] + max_coins(rows, cols, coins, curr_row + 1, curr_col)
        elif curr_col < cols - 1:
            return coins[curr_row][curr_col] + max(max_coins(rows, cols, coins, curr_row + 1, curr_col), max_coins(rows, cols, coins, curr_row, curr_col + 1))

new_coins = []
for row in cions:
    new_coins.append([-value for value in row])
min_value = - max_value(rows, cols, new_coins, 0, 0  )