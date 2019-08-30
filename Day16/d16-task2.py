def main():
    programs = list()
    counter = 0
    for program in range(ord('a'), ord('p') + 1):
        programs.append(chr(program))
    start_position = ""
    for i in programs:
        start_position += str(i)
    with open('./d16-task1.txt', 'r') as reader:
        dance_moves = reader.readline().replace("\n", "").split(",")
        for timer in range(1000000000):
            result = ""
            for i in programs:
                result += i
            if result == start_position and timer != 0:
                break
            else:
                counter += 1
            dance(dance_moves, programs)
        remaining_dances = 1000000000 % counter
        for i in range(remaining_dances):
            dance(dance_moves, programs)
    result = ""
    for i in programs:
        result += i
    print(result)


def dance(dance_moves, programs):
    for dance_move in dance_moves:
        if dance_move[0] == 's':
            for i in range(int(dance_move[1:])):
                programs.insert(0, programs[len(programs) - 1])
                del programs[len(programs) - 1]
        elif dance_move[0] == 'x':
            elements = dance_move[1:].split("/")
            first, second = int(elements[0]), int(elements[1])
            programs[first], programs[second] = programs[second], programs[first]
        elif dance_move[0] == 'p':
            first, second = programs.index(dance_move[1]), programs.index(dance_move[3])
            programs[first], programs[second] = programs[second], programs[first]


if __name__ == "__main__":
    main()
