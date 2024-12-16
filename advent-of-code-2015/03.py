#   Moves are always exactly one house to the north (^), south (v), east (>), or west (<).
#   After each move, he delivers another present to the house at his new location.
#   How many houses receive at least one present?

def house_counter(line):
    x, y = 0, 0

    visited_houses = set()
    visited_houses.add((x, y))

    for move in line:
        if move == '^':
            y += 1
        elif move == 'v':
            y -= 1
        elif move == '>':
            x += 1
        elif move == '<':
            x -= 1

        visited_houses.add((x, y))

    return len(visited_houses)


def house_counter_2(line):
    x_santa, y_santa = 0, 0
    x_robo, y_robo = 0, 0
    step = 0

    visited_houses = set()
    visited_houses.add((x_santa, y_santa))

    for move in line:
        if step % 2 == 0:
            if move == '^':
                y_santa += 1
            elif move == 'v':
                y_santa -= 1
            elif move == '>':
                x_santa += 1
            elif move == '<':
                x_santa -= 1
        else:
            if move == '^':
                y_robo += 1
            elif move == 'v':
                y_robo -= 1
            elif move == '>':
                x_robo += 1
            elif move == '<':
                x_robo -= 1

        step += 1
        visited_houses.add((x_santa, y_santa))
        visited_houses.add((x_robo, y_robo))

    return len(visited_houses)


line = input().strip()
print(house_counter(line))
print(house_counter_2(line))
