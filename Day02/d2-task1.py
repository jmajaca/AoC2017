def main():
    sum = 0
    with open('C:/Users/Josip/Documents/Python/AoC17/d2-task1.txt', 'r') as reader:
        line = reader.readline()
        while line != '':  # The EOF char is an empty string
            line = line.replace("\n", "")
            elements = line.split("\t")
            min = int(elements[0])
            max = int(elements[0])
            for element in elements:
                if int(element) > max:
                    max = int(element)
                if int(element) < min:
                    min = int(element)
            sum += (max-min)
            line = reader.readline()
    print(sum)



if __name__ == "__main__":
    main()
