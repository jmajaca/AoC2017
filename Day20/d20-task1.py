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
    print(distance(particles))


def calculate(particles):
    for key in particles:
        particle = particles[key]
        for i in range(3):
            particle[1][i] += particle[2][i]
            particle[0][i] += particle[1][i]


def distance(particles):
    min_dist = 0
    result_key = 0
    for i in range(3):
        min_dist += abs(particles[0][0][i])
    for key in particles:
        particle = particles[key]
        current_dist = 0
        for i in range(3):
            current_dist += abs(particle[0][i])
        if min_dist > current_dist:
            min_dist = current_dist
            result_key = key
    return result_key


if __name__ == "__main__":
    main()
