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

    def get_disc_programs(self):
        return self.disc_programs

    def get_wright(self):
        return self.weight


def make_program(name, weight, disc_programs):
    program = Program(name, weight, disc_programs)
    return program


def search_bottom_program(program_list, programs_bellow):
    for element in program_list:
        if not programs_bellow.__contains__(element.get_name()):
            print(element)
            break


def weight_of_disc(program, weight_sum, program_list):
    weight_list = list()
    found = False
    for element in program.get_disc_programs():
        for el in program_list:
            if el.get_name() == element:
                temp_sum = weight_of_disc(el, weight_sum, program_list)
                weight_list.append(temp_sum)
                weight_sum += temp_sum
    sum = 0
    for i in weight_list:
        sum += i
        if weight_list.count(i) == 1:
            found = True
    if found:
        count = 0
        for element in program.get_disc_programs():
            for el in program_list:
                if el.get_name() == element:
                    print(el.get_name() + ' ' + str(el.get_wright()) + ' ' + str(weight_list[count]))
                    count += 1
        print("\n")
    for element in program_list:
        if element.get_name() == program.get_name():
            return element.get_wright() + sum
    return 0

def main():
    program_list = list()
    programs_bellow = list()
    with open('C:/Users/Josip/Documents/Python/AoC17/d7-task2.txt', 'r') as reader:
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
                left_elements = list()
            program_list.append(make_program(right_elements[0], int(right_elements[1]), list(left_elements)))
            line = reader.readline()
    for element in program_list:
        sum = 0
        sum = weight_of_disc(element, sum, program_list)


if __name__ == "__main__":
    main()
