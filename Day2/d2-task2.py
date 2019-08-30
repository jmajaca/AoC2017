def main():
    sum = 0
    with open('C:/Users/Josip/Documents/Python/AoC17/d2-task2.txt', 'r') as reader:
        line = reader.readline()
        while line != '':
            line = line.replace("\n", "")
            elements = line.split("\t")
            for element in elements:
                result = divider(int(element), list(map(int, elements)))
                if result != 0:
                    sum += result
                    break
            line = reader.readline()
    print(sum)


def divider(num, nums):
    for i in nums:
        if i != num and i % num == 0:
            return int(i / num)
    return 0


if __name__ == "__main__":
    main()