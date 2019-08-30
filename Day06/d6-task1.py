import sys


def main():
    sys.argv.pop(0)
    memory = list(map(int, sys.argv))
    past_states = list()
    seen = False
    counter = 0
    while 1:
        reallocate_memory(memory, get_index_of_biggest_number(memory))
        if past_states.__contains__(memory):
           if not seen:
               seen = True
           else:
               print(counter)
               break
        else:
            past_states.append(list(memory))
        counter += 1


def reallocate_memory(list, start_index):
    counter = 0
    start_value = list[start_index]
    while start_value != counter:
        counter += 1
        current_index = (start_index + counter) % len(list)
        list[current_index] += 1
        list[start_index] -= 1


def get_index_of_biggest_number(list_to_check):
    index = 0
    for i in range(1, len(list_to_check)):
        if list_to_check[i] > list_to_check[index]:
            index = i
    return index


if __name__ == "__main__":
    main()
