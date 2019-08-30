def main():
    counter = 0
    with open('C:/Users/Josip/Documents/Python/AoC17/d4-task1.txt', 'r') as reader:
        line = reader.readline()
        while line != '':
            valid = True
            line = line.replace("\n", "")
            words = line.split(" ")
            passphrase = list()
            for word in words:
                if anagram_in_list(passphrase, word):
                    valid = False
                    break
                else:
                    passphrase.append(word)
            if valid:
                counter += 1
            line = reader.readline()
    print(counter)


def anagram_in_list(list_to_check, word):
    for element in list_to_check:
        if anagram(element, word):
            return True
    return False


def anagram(word1, word2):
    counter = 0
    for char in word1:
        if word2.__contains__(char):
            word2 = word2.replace(char, "*", 1)
            counter += 1
    if counter == len(word1) == len(word2):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
