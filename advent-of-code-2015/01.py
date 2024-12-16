#   An opening parenthesis, (, means he should go up one floor,
#   and a closing parenthesis, ), means he should go down one floor.

def basement(line):
    level = 0
    steps = 0

    for i in line:
        if level == -1:
            return steps
        else:
            steps += 1
            if i == ')':
                level -= 1
            if i == '(':
                level += 1

    return steps


def counter(line):
    level = 0

    for i in line:
        if i == ')':
            level -= 1
        if i == '(':
            level += 1

    return level


line = input()

print(counter(line))
print(basement(line))
