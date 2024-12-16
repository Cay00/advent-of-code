#   The map shows the current position of the guard with ^ (to indicate the guard is currently facing up
#   from the perspective of the map). Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

#   Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:
#       - If there is something directly in front of you, turn right 90 degrees.
#       - Otherwise, take a step forward.

#   test data 1:
#   ....#.....
#   .........#
#   ..........
#   ..#.......
#   .......#..
#   ..........
#   .#..^.....
#   ........#.
#   #.........
#   ......#...

#   test answer 1: 41

def walker(grid):
    x = len(grid)
    y = len(grid[0])
    visited_positions = set()

    directions = [
        (-1, 0),  # 0 up
        (0, 1),  # 1 right
        (1, 0),  # 2 down
        (0, -1),  # 3 left
    ]

    # Find the starting position of the guard ('^')
    start_x, start_y, direction = 0, 0, 0
    for r in range(x):
        # r - row number
        for c in range(y):
            # c - column number
            if grid[r][c] == '^':
                start_x, start_y = r, c
                visited_positions.add((r, c))
                break

    # Moving guard position
    x_pos, y_pos = start_x, start_y

    while True:
        # Check if the guard has touched the boundary
        if x_pos == 0 or x_pos == x - 1 or y_pos == 0 or y_pos == y - 1:
            break

        # Check the next position in the current direction
        next_x = x_pos + directions[direction][0]
        next_y = y_pos + directions[direction][1]

        if 0 <= next_x < x and 0 <= next_y < y and grid[next_x][next_y] != '#':
            # Move forward if the next position is within bounds and not blocked
            x_pos, y_pos = next_x, next_y
            if (x_pos, y_pos) not in visited_positions:
                visited_positions.add((x_pos, y_pos))  # Mark as visited
        else:
            # Turn right (90 degrees clockwise) if blocked
            direction = (direction + 1) % 4

    return len(visited_positions)


grid = []

while True:
    line = input().strip()
    if not line:
        break
    grid.append(line)

print(walker(grid))
