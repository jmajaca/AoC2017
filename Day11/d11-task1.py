def main():
    vertical_counter = 0
    right_counter = 0
    left_counter = 0
    with open('C:/Users/Josip/Documents/Python/AoC17/d11-task1.txt', 'r') as reader:
        steps = reader.readline().split(",")
        #ovdje napravi scan i konverziju ovisno o redoslijedu i smjeru
        #konverzija ovisi o prvom koraku kombe i ide li sljedeci u plus ili minus
        #vertical + left + right = vertical
        #nakon konverzije bi ovo dole trebalo radit
        for step in steps:
            if step == 'n':
                vertical_counter += 1
            elif step == 's':
                vertical_counter -= 1
            elif step == 'ne':
                right_counter += 1
            elif step == 'sw':
                right_counter -= 1
            elif step == 'nw':
                left_counter += 1
            elif step == 'se':
                left_counter -= 1
    vertical_counter = abs(vertical_counter)
    right_counter = abs(right_counter)
    left_counter = abs(left_counter)
    while right_counter != 0 and left_counter != 0:
        right_counter -= 1
        left_counter -= 1
        vertical_counter += 1
    if right_counter == 0:
        total_steps = left_counter + vertical_counter
    else:
        total_steps = right_counter + vertical_counter
    print(total_steps)


if __name__ == "__main__":
    main()
