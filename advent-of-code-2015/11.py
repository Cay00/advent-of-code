def has_straight(line):
    # Increasing straight of at least three letters
    for i in range(len(line) - 2):
        if ord(line[i]) + 1 == ord(line[i + 1]) and ord(line[i]) + 2 == ord(line[i + 2]):
            return True
    return False


def invalid_letters(line):
    for i in line:
        if i == 'i' or i == 'o' or i == 'l':
            return False
    return True


def pairs(line):
    pair = 0
    i = 0

    while i < len(line) - 1:
        if line[i] == line[i + 1]:
            pair += 1
            i += 2
        else:
            i += 1
        if pair >= 2:
            return True

    return False


def changer(line):
    line = list(line)
    for i in range(len(line) - 1, -1, -1):
        if line[i] == 'z':
            line[i] = 'a'
        else:
            line[i] = chr(ord(line[i]) + 1)
            break
    return ''.join(line)


def is_valid(line):
    while not (has_straight(line) and invalid_letters(line) and pairs(line)):
        line = changer(line)
    return line


line = "hxbxwxba"

first = is_valid(line)
print(first)

second = is_valid(changer(first))
print(second)
