def main():
    counter = 0
    with open('C:/Users/Josip/Documents/Python/AoC17/d4-task1.txt', 'r') as reader:
        line = reader.readline()
        while line != '':
            valid = True
            line = reader.readline()
            line = line.replace("\n", "")
            words = line.split(" ")
            passphrase = list()
            for word in words:
                if passphrase.__contains__(word):
                    valid = False
                    break
                else:
                    passphrase.append(word)
            if valid:
                counter += 1
    print(counter)


if __name__ == "__main__":
    main()