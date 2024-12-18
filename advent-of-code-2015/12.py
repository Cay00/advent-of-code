def counter(line):
    total = 0
    number = 0

    for i in range(1, len(line)):
        if line[i].isdigit() and line[i - 1].isdigit():
            number *= 10
            if number > 0:
                # Number >= 10
                number += int(line[i])
            else:
                # Number <= -10
                number -= int(line[i])
        elif line[i].isdigit() and line[i - 1] != '-':
            # Number >= 0
            number += int(line[i])
        elif line[i].isdigit() and line[i - 1] == '-':
            # Number <= 0
            number -= int(line[i])
        else:
            total += number
            number = 0

    return total


line = input()
sum = counter(line)
print(sum)
