def main():
    neighborhood = dict()
    connections = list()
    with open('C:/Users/Josip/Documents/Python/AoC17/d12-task2.txt', 'r') as reader:
        line = reader.readline()
        while line != '':
            line = line.replace("\n", "")
            elements = line.split(" <-> ")
            neighborhood[int(elements[0])] = [int(element) for element in elements[1].split(", ")]
            line = reader.readline()
    counter = 0
    while len(neighborhood) > 0:
        connections.append(next(iter(neighborhood.keys())))
        get_connections(neighborhood, connections[0], connections)
        for element in connections:
            del neighborhood[int(element)]
        counter += 1
        connections = list()
    print(counter)


def get_connections(neighborhood, program, connections):
    for element in neighborhood[program]:
        if not connections.__contains__(element):
            connections.append(element)
            get_connections(neighborhood, element, connections)


if __name__ == "__main__":
    main()
