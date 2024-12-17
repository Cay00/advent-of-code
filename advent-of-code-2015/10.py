def sequences(line):
    new_line = ""
    actual_number = line[0]
    value = 0

    for number in range(len(line)):
        if line[number] == actual_number:
            value += 1
        else:
            new_line += str(value) + str(actual_number)
            actual_number = line[number]
            value = 1
        if number == len(line) - 1:
            new_line += str(value) + str(actual_number)

    return new_line


line = "1113122113"

for i in range(50):
    line = sequences(line)
    if i == 40 - 1:
        print(len(line))
print(len(line))
