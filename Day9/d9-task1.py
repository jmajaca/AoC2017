def check_for_exclamation(line, i):
    if line[i] == '!':
        i += 2
        i = check_for_exclamation(line, i)
    return i


def check_for_garbage(line, i):
    if line[i] == '<':
        for index in range(i + 1, len(line)):
            if line[index] == '>':
                return index + 1
    else:
        return i


def calculate_score(line):
    counter = 0
    for i in range(0, len(line)-1):
        if line[i] == "{":
            counter += 1
            if line[i+1] == "}":
                del line[i+1]
                del line[i]
                return counter


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
        while i < len(line_wo_exclamation):
            i = check_for_garbage(line_wo_exclamation, i)
            line_wo_garbage += str(line_wo_exclamation[i])
            i += 1
        line_wo_garbage = line_wo_garbage.replace(",", "")
        total_score = 0
        list_line = list(line_wo_garbage)
        while len(list_line) != 0:
            total_score += calculate_score(list_line)
        print(total_score)


if __name__ == "__main__":
    main()
