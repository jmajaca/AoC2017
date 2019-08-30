factor = [16807, 48271]
devider = 2147483647


def main():
  times = 40000000
  counter = 0
  values = list()
  with open('C:/Users/Josip/Documents/Python/AoC17/d15-task1.txt', 'r') as reader:
    for i in range(2):
      line = reader.readline()
      line = line.replace("\n", "")
      elements = line.split(" ")
      values.append(int(elements[4]))
  while times != 0:
    generate(values)
    counter = judge(values, counter)
    times -= 1
  print(counter)


def judge(values, counter):
  bit_values = list()
  for i in range(2):
    bit_values.append(bin(values[i] & 0xFFFF))
  if bit_values[0] == bit_values[1]:
    counter += 1
  return counter


def generate(values):
  global factor
  global devider
  for i in range(2):
    values[i] = int((values[i] * factor[i]) % devider)


if __name__ == "__main__":
  main()
