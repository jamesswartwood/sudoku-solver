### Imports ###

from time import time


### Global definitions ###

# size of row/col/group
M = 9

# initial grid where '0' means empty cell
grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
        [4, 0, 7, 0, 0, 0, 2, 0, 8],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 8, 1, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 6, 0, 0, 7, 2],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 3, 0, 0, 0, 6, 0, 4]]


### Function definitions ###

'''
Prints sudoku grid in terminal.

Arguments:
    `sudoku` = matrix representing sudoku puzzle
'''
def display_sudoku(sudoku):
    for i in range(9):
        for j in range(9):
            cell = sudoku[i][j]
            if cell == 0 or isinstance(cell, set):
                print('.', end='')
            else:
                print(cell, end='')
            if (j + 1) % 3 == 0 and j < 8:
                print(' |', end='')

            if j != 8:
                print('  ', end='')
        print('\n', end='')
        if (i + 1) % 3 == 0 and i < 8:
            print("--------+----------+---------\n", end='')

'''
Checks if number is valid in specified cell.

Arguments:
    `grid` = matrix representing sudoku puzzle
    `row` = row index
    `col` = column index
    `num` = number to validate
'''
def validate_number(grid, row, col, num):
    # check if num is already in row
    for x in range(9):
        if grid[row][x] == num:
            return False

    # check if num is already in column
    for x in range(9):
        if grid[x][col] == num:
            return False

    # check if num in already in group
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False

    # if none of the above cases were triggered, the number is valid
    return True

'''
Recursive helper function that eventually solves a sudoku grid.

Arguments:
    `grid` = matrix representing sudoku puzzle
    `row` = target row in iteration
    `col` = target column in iteration
'''
def solve_sudoku_helper(grid, row, col):
    # case: size has been reached
    if (row == M - 1 and col == M):
        return True
    # case: end column reached, row completed
    if col == M:
        row += 1
        col = 0
    # case: valid row and column specified
    if grid[row][col] > 0:
        return solve_sudoku_helper(grid, row, col + 1)

    # iterate through potential number solutions for cell (eg. 1-9)
    for num in range(1, M + 1, 1):
        # check number validity
        if validate_number(grid, row, col, num):
            # update grid with potential solution to cell
            grid[row][col] = num
            # recurse to further iteration
            if solve_sudoku_helper(grid, row, col + 1):
                return True
        # if further iterations proved solution invalid, reset cell
        grid[row][col] = 0
    # if all potential number solutions prove invalid, report the find
    return False

'''
Sukodu solver function that triggers recursive backtrace solution.

Arguments:
    `grid` = matrix representing sudoku puzzle
'''
def solve_sudoku(grid):
    # call helper function starting at row and col 0
    return solve_sudoku_helper(grid, 0, 0)


### Main program runtime ###

if __name__ == "__main__":
    start_time = time()
    solved = solve_sudoku(grid)
    runtime = time() - start_time

    if solved:
        print(f"Solution found in {round(runtime * 1000)} milliseconds:")
        display_sudoku(grid)
    else:
        print(f"Determined that no solution exists in {round(runtime * 1000)} milliseconds")