import sys


def main():
    sys.argv.pop(0)
    message = list(map(int, sys.argv))
    index = 0
    counter = 0
    while index in range(0, len(sys.argv)):
        step = message[index]
        if step >= 3:
            message[index] = step - 1
        else:
            message[index] = step + 1
        index += step
        counter += 1
    print(counter)


if __name__ == "__main__":
    main()
