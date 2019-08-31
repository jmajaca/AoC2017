def main():
    operations = []
    registers = dict()
    with open('./d18-task.txt', 'r') as reader:
        line = reader.readline()
        while line != '':
            line = line.replace("\n", "")
            elements = line.split(" ")
            operations.append((elements[0], elements[1], elements[2] if len(elements) == 3 else None))
            if not registers.__contains__(elements[1]) and elements[0] != 'jgz':
                registers[(elements[1])] = 0
            line = reader.readline()
    index = 0
    while index < len(operations):
        if operations[index][0] == 'snd':
            last_frequency = int(registers[operations[index][1]])
        elif operations[index][0] == 'set':
            registers[operations[index][1]] = int(operations[index][2]) if not registers.__contains__(
                operations[index][2]) else registers[operations[index][2]]
        elif operations[index][0] == 'add':
            registers[operations[index][1]] += int(operations[index][2]) if not registers.__contains__(
                operations[index][2]) else registers[operations[index][2]]
        elif operations[index][0] == 'mul':
            registers[operations[index][1]] *= int(operations[index][2]) if not registers.__contains__(
                operations[index][2]) else registers[operations[index][2]]
        elif operations[index][0] == 'mod':
            registers[operations[index][1]] %= int(operations[index][2]) if not registers.__contains__(
                operations[index][2]) else registers[operations[index][2]]
        elif operations[index][0] == 'rcv':
            if registers[operations[index][1]] != 0:
                print(last_frequency)
                break
        elif operations[index][0] == 'jgz':
            jump = 0
            if registers.__contains__(operations[index][1]):
                if registers[operations[index][1]] > 0:
                    jump = int(operations[index][2]) if not registers.__contains__(
                        operations[index][2]) else registers[operations[index][2]]
            elif int(operations[index][2]) > 0:
                jump = int(operations[index][2])
            if jump != 0:
                index += (jump - 1)
        index += 1


if __name__ == "__main__":
    main()
