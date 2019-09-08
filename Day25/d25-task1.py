from blist import blist


def main():
    states = dict()
    tape = blist()
    tape.append(0)
    cursor = 0
    with open('./d25-task1.txt', 'r') as reader:
        current_state = reader.readline().split(" ")[3][:1]
        steps = int(reader.readline().split(" ")[5])
        line = reader.readline()
        while line != '':
            read_state = reader.readline().split(" ")[2][:1]
            for i in range(2):
                read_value = reader.readline().split(" ")[7][:1]
                new_value = reader.readline().split(" ")[8][:1]
                new_direction = reader.readline().split(" ")[10].replace(".\n", "")
                new_state = reader.readline().split(" ")[8][:1]
                states[read_state, int(read_value)] = new_state, int(new_value), new_direction
            line = reader.readline()
        for i in range(steps):
            instructions = states[current_state, tape[cursor]]
            current_state = instructions[0]
            if instructions[2] == 'right':
                tape[cursor] = instructions[1]
                cursor += 1
                if cursor >= len(tape):
                    tape = tape + [0]
            else:
                tape[cursor] = instructions[1]
                cursor -= 1
                if cursor < 0:
                    tape = [0] + tape
                    cursor = 0
        counter = 0
        for i in range(len(tape)):
            if tape[i] == 1:
                counter += 1
        print(counter)


if _name_ == "_main_":
    main()
