import sys
import numpy as np

matrix_row = 11
matrix_column = 11
current_row = 5
current_column = 5
found = False


def main():
    matrix = np.zeros((matrix_row, matrix_column))
    matrix[current_row][current_column] = 1
    step = 0
    while current_column in range(0, matrix_column) and current_row in range(0, matrix_row) and not found:
        step += 1
        right(step, matrix)
        top(step, matrix)
        step += 1
        left(step, matrix)
        bottom(step, matrix)


def bottom(step, matrix):
    global current_row
    for row in range(1, step+1):
        current_row += 1
        if in_bounds(current_row, current_column):
            matrix[current_row][current_column] = search_nearby(matrix, current_row, current_column)
            is_found(matrix[current_row][current_column])


def top(step, matrix):
    global current_row
    for row in range(1, step+1):
        current_row -= 1
        if in_bounds(current_row, current_column):
            matrix[current_row][current_column] = search_nearby(matrix, current_row, current_column)
            is_found(matrix[current_row][current_column])


def left(step, matrix):
    global current_column
    for column in range(1, step+1):
        current_column -= 1
        if in_bounds(current_row, current_column):
            matrix[current_row][current_column] = search_nearby(matrix, current_row, current_column)
            is_found(matrix[current_row][current_column])


def right(step, matrix):
    global found
    global current_column
    for column in range(1, step+1):
        current_column += 1
        if in_bounds(current_row, current_column):
            matrix[current_row][current_column] = search_nearby(matrix, current_row, current_column)
            is_found(matrix[current_row][current_column])


def is_found(value):
    global found
    if value > int(sys.argv[1]):
        found = True
        print(int(value))


def in_bounds(i, j):
    if i >= matrix_row or i < 0:
        return False
    if j >= matrix_column or j < 0:
        return False
    return True


def search_nearby(matrix, i, j):
    sum = 0
    for row in (i-1, i, i+1):
        if row >= matrix_row or row < 0:
            continue
        for column in (j-1, j, j+1):
            if column >= matrix_column or column < 0:
                continue
            sum += matrix[row][column]
    return sum


if __name__ == "__main__":
    main()
