def main():
    number_list = list()
    current_position = 0
    step = 0
    for num in range(0, 256):
        number_list.append(num)
    with open('C:/Users/Josip/Documents/Python/AoC17/d10-task1.txt', 'r') as reader:
        line = reader.readline()
        lengths = list(map(int, line.split(",")))
        for length in lengths:
            if length > len(number_list):
                break
            for i in range(0, int(length/2)):
                minus = i
                i += current_position
                i %= len(number_list)
                temp = number_list[i]
                number_list[i] = number_list[int((length + current_position) % len(number_list) - minus - 1)]
                number_list[int((length + current_position) % len(number_list) - minus - 1)] = temp
            current_position = (current_position + step + length) % len(number_list)
            step += 1
    print(str(number_list[0] * number_list[1]))


if __name__ == "__main__":
    main()
