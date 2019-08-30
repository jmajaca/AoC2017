import sys


def main():
    found = False
    for new_block_value in (2, 4, 6, 8):
        if found:
            break
        old_block_value = 1
        result = 1
        temp_value = new_block_value - old_block_value
        while new_block_value <= int(sys.argv[1]):
            old_block_value = new_block_value
            new_block_value = temp_value + 8 + new_block_value
            temp_value = new_block_value - old_block_value
            result += 1
            for step in range(0, result+1):
                if new_block_value + step == int(sys.argv[1]) or new_block_value - step == int(sys.argv[1]):
                    print(str(result + step))
                    found = True


if __name__ == "__main__":
    main()
