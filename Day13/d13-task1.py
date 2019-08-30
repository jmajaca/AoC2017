def main():
    layers = dict()
    scanner = dict()
    with open('C:/Users/Josip/Documents/Python/AoC17/d13-task1.txt', 'r') as reader:
        line = reader.readline()
        while line != '':
            elements = line.split(": ")
            layers[int(elements[0])] = int(elements[1])
            scanner[int(elements[0])] = (0, True)
            line = reader.readline()
    sum = 0
    for current_layer in range(max(iter(layers.keys())) + 1):
        if scanner.__contains__(current_layer):
            index, direction = scanner[current_layer]
            if index == 0:
                sum += current_layer * layers[current_layer]
        scan(scanner, layers)
    print(sum)


def scan(scanner, layers):
    for key in scanner:
        position, direction = scanner[key]
        if (position + 1) >= layers[key] and direction:
            scanner[key] = (layers[key] - (position + 1) % layers[key] - 2, not direction)
        elif position - 1 < 0 and not direction:
            scanner[key] = (1, not direction)
        else:
            if direction:
                scanner[key] = (position + 1, direction)
            else:
                scanner[key] = (position - 1, direction)


if __name__ == "__main__":
    main()
