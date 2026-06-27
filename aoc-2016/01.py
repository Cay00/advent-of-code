def distance(instructions):
    # 0 = North, 1 = East, 2 = South, 3 = West
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # dx, dy

    x, y = 0, 0
    current_direction = 0  # North
    steps = instructions.split(', ')

    for step in steps:
        turn = step[0]
        distance = int(step[1:])

        if turn == "R":
            current_direction = (current_direction + 1) % 4
        elif turn == "L":
            current_direction = (current_direction - 1) % 4

        dx, dy = directions[current_direction]
        x += dx * distance
        y += dy * distance

    return abs(x) + abs(y)


def location(instructions):
    # 0 = North, 1 = East, 2 = South, 3 = West
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # dx, dy

    x, y = 0, 0
    current_direction = 0  # North
    steps = instructions.split(', ')
    visited = set()
    visited.add((x, y))

    for step in steps:
        turn = step[0]
        distance = int(step[1:])

        if turn == "R":
            current_direction = (current_direction + 1) % 4
        elif turn == "L":
            current_direction = (current_direction - 1) % 4

        for _ in range(distance):
            dx, dy = directions[current_direction]
            x += dx
            y += dy

            if (x, y) in visited:
                return abs(x) + abs(y)
            visited.add((x, y))

    return None


instructions = input()
print(distance(instructions))
print(location(instructions))
