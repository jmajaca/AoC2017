def main():
    current_position = 0
    step = 0
    number_list = [i for i in range(256)]
    with open('C:/Users/Josip/Documents/Python/AoC17/d10-task2.txt', 'r') as reader:
        line = reader.readline()
        lengths = list(map(ord, line)) + [17, 31, 73, 47, 23]
        for iterations in range(64):
            for length in lengths:
                if length > len(number_list):
                    break
                for i in range(0, int(length/2)):
                    current_index = (i + current_position) % len(number_list)
                    temp = number_list[current_index]
                    number_list[current_index] = number_list[int((length + current_position) % len(number_list) - i-1)]
                    number_list[int((length + current_position) % len(number_list) - i - 1)] = temp
                current_position = (current_position + step + length) % len(number_list)
                step += 1
    dense_hash = list()
    for i in range(0, 16):
        result = number_list[16*i]
        for j in range(1, 16):
            result ^= number_list[i*16+j]
        dense_hash.append(result)
    result_hash = ""
    for i in dense_hash:
        result_hash += (str((hex(i)[2:]) if len((hex(i)[2:])) > 1 else '0' + str(hex(i)[2:])))
    print(result_hash)


if __name__ == "__main__":
    main()
