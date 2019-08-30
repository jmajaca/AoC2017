import sys


def main():
    sys.argv.pop(0)
    message = list(sys.argv)
    index = 0
    counter = 0
    while index in range(0, len(sys.argv)):
        step = message[index]
        message[index] = str(int(step) + 1)
        if step == 0:
            continue
        else:
            index += int(step)
        counter += 1
    print(counter)


if __name__ == "__main__":
    main()
