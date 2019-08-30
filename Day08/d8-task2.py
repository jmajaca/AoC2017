def check_condition(dictionary_value, operation, num_value):
    if operation == ">":
        if dictionary_value > num_value:
            return True
        else:
            return False
    elif operation == "<":
        if dictionary_value < num_value:
            return True
        else:
            return False
    elif operation == ">=":
        if dictionary_value >= num_value:
            return True
        else:
            return False
    elif operation == "<=":
        if dictionary_value <= num_value:
            return True
        else:
            return False
    elif operation == "==":
        if dictionary_value == num_value:
            return True
        else:
            return False
    elif operation == "!=":
        if dictionary_value != num_value:
            return True
        else:
            return False


def main():
    variables = dict()
    max_value = 0
    with open('C:/Users/Josip/Documents/Python/AoC17/d8-task1.txt', 'r') as reader:
        line = reader.readline()
        while line != '':
            elements = line.split(" ")
            if elements[0] not in variables:
                variables[elements[0]] = 0
            if elements[1] == "inc":
                increment = True
            else:
                increment = False
            if elements[4] not in variables:
                variables[elements[4]] = 0
            if check_condition(variables[elements[4]], elements[5], int(elements[6])):
                if increment:
                    variables[elements[0]] += int(elements[2])
                else:
                    variables[elements[0]] -= int(elements[2])
            if max_value < variables[elements[0]]:
                max_value = variables[elements[0]]
            line = reader.readline()
    print(max_value)


if __name__ == "__main__":
    main()

