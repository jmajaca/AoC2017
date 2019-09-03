def main():
    particles = dict()
    with open('./d20-task.txt', 'r') as reader:
        line = reader.readline()
        index = 0
        while line != '':
            elements = line.replace("=<", "").replace(">", "").replace("a", "").replace("\n", "").replace(
                "p", "").replace("v", "").split(", ")
            sub_elements = []
            for element in elements:
                sub_elements.append(list(map(int, element.replace(" ", "").split(","))))
            particles[index] = sub_elements
            line = reader.readline()
            index += 1
    for i in range(1000):
        calculate(particles)
    print(len(particles))


def calculate(particles):
    positions = dict()
    deletion_list = set()
    for key in particles:
        particle = particles[key]
        for i in range(3):
            particle[1][i] += particle[2][i]
            particle[0][i] += particle[1][i]
        key_string = ''
        for element in particle[0]:
            key_string += str(element)
        if not positions.__contains__(key_string):
            positions[key_string] = set()
            positions[key_string].add(key)
        else:
            positions[key_string].add(key)
            deletion_list.add(key_string)
    for i in deletion_list:
        position = positions[i]
        for element in position:
            del particles[element]


if __name__ == "__main__":
    main()
