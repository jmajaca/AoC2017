import numpy


max_column = 0
max_row = 0
counter = 0


def main():
    global counter
    global max_row
    global max_column
    line_list = []
    matrix_margin = 1000
    with open('./d22-task1.txt', 'r') as reader:
        line = reader.readline()
        while line != '':
            line = line.replace("\n", "")
            line_list.append(line)
            line = reader.readline()
    max_column = len(line_list[0]) + matrix_margin
    max_row = len(line_list) + matrix_margin
    current_position = [int(max_row/2), int(max_column/2)]
    matrix = numpy.zeros([max_row, max_column], dtype=bool)
    for row in range(max_row-matrix_margin):
        line = line_list[row]
        for column in range(len(line)):
            if line[column] == '#':
                matrix[row+int(matrix_margin/2)][column+int(matrix_margin/2)] = True
    direction = 'up'
    for i in range(10000):
        direction = virus_work(matrix, current_position, direction)
    print(counter)


def virus_work(matrix, current_position, direction):
    global counter
    if not matrix[current_position[0]][current_position[1]]:
        matrix[current_position[0]][current_position[1]] = True
        counter += 1
        if direction == 'up':
            current_position[1] -= 1
            return 'left'
        elif direction == 'down':
            current_position[1] += 1
            return 'right'
        elif direction == 'right':
            current_position[0] -= 1
            return 'up'
        else:
            current_position[0] += 1
            return 'down'
    else:
        matrix[current_position[0]][current_position[1]] = False
        if direction == 'up':
            current_position[1] += 1
            return 'right'
        elif direction == 'down':
            current_position[1] -= 1
            return 'left'
        elif direction == 'right':
            current_position[0] += 1
            return 'down'
        else:
            current_position[0] -= 1
            return 'up'


if __name__ == "__main__":
    main()
