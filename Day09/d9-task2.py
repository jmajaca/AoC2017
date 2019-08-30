def check_for_exclamation(line, i):
    if line[i] == '!':
        i += 2
        i = check_for_exclamation(line, i)
    return i


def check_for_garbage(line, i):
    if line[i] == '<':
        for index in range(i + 1, len(line)):
            if line[index] == '>':
                return index + 1, True
    else:
        return i, False


def main():
    with open('C:/Users/Josip/Documents/Python/AoC17/d9-task1.txt', 'r') as reader:
        line = reader.readline()
        line = line.replace("\n", "")
        line_wo_exclamation = ""
        i = 0
        while i < len(line):
            i = check_for_exclamation(line, i)
            line_wo_exclamation += str(line[i])
            i += 1
        i = 0
        line_wo_garbage = ""
        garbage_counter = 0
        while i < len(line_wo_exclamation):
            response = check_for_garbage(line_wo_exclamation, i)
            i = response[0]
            if response[1]:
                garbage_counter += 1
            line_wo_garbage += str(line_wo_exclamation[i])
            i += 1
        print(str(len(line_wo_exclamation) - len(line_wo_garbage) - garbage_counter * 2))


if __name__ == "__main__":
    main()
