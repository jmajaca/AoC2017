factor = [16807, 48271]
devider = 2147483647


def main():
  counter = 0
  values = list()
  with open('C:/Users/Josip/Documents/Python/AoC17/d15-task2.txt', 'r') as reader:
    for i in range(2):
      line = reader.readline()
      line = line.replace("\n", "")
      elements = line.split(" ")
      values.append(int(elements[4]))
  for i in range(5000000):
    if bin(generate(values, 0) & 0xFFFF) == bin(generate(values, 1) & 0xFFFF):
        counter += 1
  print(counter)


def generate(values, i):
  global factor
  global devider
  values[i] = int((values[i] * factor[i]) % devider)
  if i == 0:
      while values[i] % 4 != 0:
          values[i] = int((values[i] * factor[i]) % devider)
      return values[i]
  if i == 1:
      while values[i] % 8 != 0:
          values[i] = int((values[i] * factor[i]) % devider)
      return values[i]


if __name__ == "__main__":
  main()