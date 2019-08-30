def main():
    buffer = [0]
    with open('./d17-task1.txt', 'r') as reader:
        step = int(reader.readline().replace("\n", ""))
        current_position = 0
        for i in range(1, 2018):
            for index in range(current_position, step + current_position):
                index = (index + 1) % len(buffer)
            buffer.insert(index + 1, i)
            current_position = index + 1
        print(buffer[(buffer.index(2017) + 1) % len(buffer)])


if __name__ == "__main__":
    main()
