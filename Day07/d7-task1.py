class Program(object):
    name = ''
    weight = 0
    disc_programs = list()

    def __init__(self, name, weight, disc_programs):
        self.name = name
        self.weight = weight
        self.disc_programs = disc_programs

    def __repr__(self):
        return "name: " + self.name + " weight: " + str(self.weight) + " disc_programs: " + str(self.disc_programs) + "\n"

    def get_name(self):
        return self.name


def make_program(name, weight, disc_programs):
    program = Program(name, weight, disc_programs)
    return program


def search_bottom_program(program_list, programs_bellow):
    for element in program_list:
        if not programs_bellow.__contains__(element.get_name()):
            print(element)
            break


def main():
    program_list = list()
    programs_bellow = list()
    with open('C:/Users/Josip/Documents/Python/AoC17/d7-task1.txt', 'r') as reader:
        line = reader.readline()
        while line != '':
            line = line.replace("\n", "")
            elements = line.split(" -> ")
            right_elements = elements[0].split(" ")
            right_elements[1] = right_elements[1].replace("(", "").replace(")", "")
            if len(elements) >= 2:
                left_elements = elements[1].split(", ")
                for element in left_elements:
                    programs_bellow.append(element)
            else:
                left_elements = ""
            program_list.append(make_program(right_elements[0], int(right_elements[1]), list(left_elements)))
            line = reader.readline()
    search_bottom_program(program_list, programs_bellow)


if __name__ == "__main__":
    main()
