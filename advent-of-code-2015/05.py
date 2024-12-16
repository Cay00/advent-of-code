def counter(line):
    vowels_type = ['a', 'e', 'i', 'o', 'u']
    restricted_type = ['ab', 'cd', 'pq', 'xy']
    vowels = 0
    double = False

    for char in line:
        for type in vowels_type:
            if char == type:
                vowels += 1
    if vowels < 3:
        return False

    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            double = True
            break
    if not double:
        return False

    for type in restricted_type:
        if type in line:
            return False

    return True


def counter_2(line):
    pair_found = False
    for i in range(len(line) - 1):
        if line[i:i + 2] in line[i + 2:]:
            pair_found = True
            break

    repeat = False
    for i in range(len(line) - 2):
        if line[i] == line[i + 2]:
            repeat = True
            break

    if pair_found and repeat:
        return True


def task(text):
    answer_1 = 0
    answer_2 = 0

    for line in text:
        if counter(line):
            answer_1 += 1
        if counter_2(line):
            answer_2 += 1

    return answer_1, answer_2


text = []

while True:
    line = input()
    if not line:
        break
    text.append(line)

print(task(text))
