import numpy
import sys

max_row = 0
max_column = 0
result_string = ''

def main():
    global max_row
    global max_column
    lines = []
    with open('./d19-task.txt', 'r') as reader:
        line = reader.readline()
        while line != '':
            line = line.replace("\n", "")
            if len(line) > max_column:
                max_column = len(line)
            lines.append(line)
            max_row += 1
            line = reader.readline()
    matrix = numpy.empty([max_row, max_column], dtype=str)
    for i in range(max_row):
        line = lines[i]
        for j in range(max_column):
            if j < len(line):
                matrix[i][j] = line[j]
                if i == 0 and line[j] == '|':
                    start_position = j
    result = search(matrix, 0, start_position, 'down')
    while True:
        result = search(matrix, result[0], result[1], result[2])
        if result[2] == 'end':
            break
    print(result_string)


def search(matrix, row, column, direction):
    global result_string
    if matrix[row][column] == '+':
        new_direction = check_cells(row, column, direction, matrix)
        return new_direction[1], new_direction[2], new_direction[0]
    elif matrix[row][column] not in ('|', '+', '-', '', ' '):
        result_string += matrix[row][column]
    elif matrix[row][column] in('', ' '):
        print(result_string)
        return 0, 0, 'end'
    if direction == 'down':
        return row + 1, column, 'down'
    elif direction == 'up':
        return row - 1, column, 'up'
    elif direction == 'right':
        return row, column + 1, 'right'
    elif direction == 'left':
        return row, column - 1, 'left'


def check_cells(row, column, direction, matrix):
    global max_row
    global max_column
    for i in (row - 1, row, row + 1):
        if i >= max_row or i < 0:
            continue
        for j in (column - 1, column, column + 1):
            if j >= max_column or j < 0:
                continue
            if row == i and column == j:
                continue
            if direction == 'down':
                if i == row - 1 and j == column:
                    continue
            elif direction == 'up':
                if i == row + 1 and j == column:
                    continue
            elif direction == 'right':
                if i == row and j == column - 1:
                    continue
            elif direction == 'left':
                if i == row and j == column + 1:
                    continue
            if matrix[i][j] != '' and matrix[i][j] != ' ':
                if i == row:
                    if j == column - 1:
                        return 'left', i, j
                    else:
                        return 'right', i, j
                elif i == row + 1:
                    return 'down', i, j
                else:
                    return 'up', i, j


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
