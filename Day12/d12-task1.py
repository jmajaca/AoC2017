def main():
    neighborhood = dict()
    connections = set()
    with open('C:/Users/Josip/Documents/Python/AoC17/d12-task1.txt', 'r') as reader:
        line = reader.readline()
        while line != '':
            line = line.replace("\n", "")
            elements = line.split(" <-> ")
            neighborhood[int(elements[0])] = [int(element) for element in elements[1].split(", ")]
            line = reader.readline()
    connections.add(0)
    get_connections(neighborhood, 0, connections)
    print(len(connections))


def get_connections(neighborhood, program, connections):
    for element in neighborhood[program]:
        if not connections.__contains__(element):
            connections.add(element)
            get_connections(neighborhood, element, connections)


if __name__ == "__main__":
    main()
