def main():
    programs = list()
    for program in range(ord('a'), ord('p') + 1):
        programs.append(chr(program))
    with open('./d16-task1.txt', 'r') as reader:
        dance_moves = reader.readline().replace("\n", "").split(",")
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
    result = ""
    for i in programs:
        result += i
    print(result)


if __name__ == "__main__":
    main()
