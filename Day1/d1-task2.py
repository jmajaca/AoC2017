import sys


def main():
    sum = 0
    input_string = sys.argv[1]
    for index in range(-1, int(len(input_string)/2) - 1):
        if input_string[index] == input_string[int(index + len(input_string)/2)]:
            sum += int(input_string[index]) * 2
        index += 1
    print(sum)


if __name__ == "__main__":
    main()