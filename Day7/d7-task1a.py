def search_bottom_program(program_list, programs_bellow):
    for element in program_list:
        if not programs_bellow.__contains__(element):
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
            program_list.append(right_elements[0])
            line = reader.readline()
    search_bottom_program(program_list, programs_bellow)


if __name__ == "__main__":
    main()
