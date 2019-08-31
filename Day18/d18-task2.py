import queue
import copy
import threading

def main():
    operations = []
    registers = dict()
    queues = []
    for i in range(2):
        queues.append(queue.Queue(100))
    with open('./d18-task.txt', 'r') as reader:
        line = reader.readline()
        while line != '':
            line = line.replace("\n", "")
            elements = line.split(" ")
            operations.append((elements[0], elements[1], elements[2] if len(elements) == 3 else None))
            if not registers.__contains__(elements[1]) and elements[0] != 'jgz':
                registers[(elements[1])] = 0
            line = reader.readline()
    try:
        for i in range(2):
            threading.Thread(target=thread_function, args=(operations, copy.deepcopy(registers), i,  queues,)).start()
    except:
        print("Error: unable to start thread")


def thread_function(operations, registers, id, queues):
    index = 0
    counter = 0
    registers['p'] = id
    while index < len(operations):
        if operations[index][0] == 'snd':
            queues[0 if id == 1 else 1].put(registers[operations[index][1]])
            counter += 1
            if id == 1:
                print('count: ' + str(counter))
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
            registers[operations[index][1]] = queues[1 if id == 1 else 0].get()
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
