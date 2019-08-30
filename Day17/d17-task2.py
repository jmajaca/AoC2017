from blist import blist


def main():
    buffer = blist([0])
    with open('./d17-task1.txt', 'r') as reader:
        step = int(reader.readline().replace("\n", ""))
        current_position = 0
        for i in range(1, 50000000):
            current_position = (current_position + step) % len(buffer) + 1
            buffer.insert(current_position, i)
        print(buffer[(buffer.index(0) + 1) % len(buffer)])


if __name__ == "__main__":
    main()
