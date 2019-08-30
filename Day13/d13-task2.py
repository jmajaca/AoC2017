def main():
    layers = dict()
    scanner = dict()
    with open('C:/Users/Josip/Documents/Python/AoC17/d13-task2.txt', 'r') as reader:
        line = reader.readline()
        while line != '':
            elements = line.split(": ")
            layers[int(elements[0])] = int(elements[1])
            scanner[int(elements[0])] = (0, True)
            line = reader.readline()
    success = False
    delay = 0
    start_scanner = dict(scanner)
    layer_length = max(iter(layers.keys())) + 1
    while not success:
        if delay != 0:
            scan(start_scanner, layers)
        scanner = dict(start_scanner)
        caught = False
        for current_layer in range(layer_length):
            if scanner.__contains__(current_layer):
                index, direction = scanner[current_layer]
                if index == 0:
                    delay += 1
                    caught = True
                    break
            scan(scanner, layers)
        if not caught:
            success = True
    print(delay)


def scan(scanner, layers):
    for key in scanner:
        position, direction = scanner[key]
        if (position + 1) >= layers[key]:
            layer_depth = layers[key]
            scanner[key] = (layer_depth - (position + 1) % layer_depth - 2, not direction)
        elif position - 1 < 0 and not direction:
            scanner[key] = (1, not direction)
        else:
            if direction:
                scanner[key] = (position + 1, direction)
            else:
                scanner[key] = (position - 1, direction)


if __name__ == "__main__":
    main()
