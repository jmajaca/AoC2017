import sys


def main():
    print(sys.argv[1])
    index = -1
    sum = 0
    input_string = sys.argv[1]
    for i in input_string:
        if i == input_string[index]:
            sum += int(input_string[index])
        index += 1
    print(sum)


if __name__ == "__main__":
    main()


