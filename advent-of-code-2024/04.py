import re


def counter(grid):
    x = len(grid)  # n
    y = len(grid[0])  # m
    target = "XMAS"
    target_len = len(target)
    count = 0

    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1)
    ]

    def is_valid(r, c):
        return 0 <= r < x and 0 <= c < y

    for r in range(x):
        # r - row number
        for c in range(y):
            # c - column number
            for dr, dc in directions:
                found = True
                for i in range(target_len):
                    nr, nc = r + dr * i, c + dc * i
                    if not is_valid(nr, nc) or grid[nr][nc] != target[i]:
                        found = False
                        break
                if found:
                    count += 1
    return count


def counter_x(grid):
    x = len(grid)  # n
    y = len(grid[0])  # m
    count = 0

    def is_valid(r, c):
        return 0 <= r < x and 0 <= c < y

    for r in range(1, x - 1):
        # r - row number
        for c in range(1, y - 1):
            # c - column number
            if (is_valid(r - 1, c - 1) and is_valid(r - 1, c + 1) and
                    is_valid(r + 1, c - 1) and is_valid(r + 1, c + 1)):

                top_left = grid[r - 1][c - 1]
                top_right = grid[r - 1][c + 1]
                center = grid[r][c]
                bottom_left = grid[r + 1][c - 1]
                bottom_right = grid[r + 1][c + 1]

                if center == 'A':
                    if ((top_left == 'M' and top_right == 'M' and bottom_left == 'S' and bottom_right == 'S')
                            or (top_left == 'S' and top_right == 'S' and bottom_left == 'M' and bottom_right == 'M')
                            or (top_left == 'M' and top_right == 'S' and bottom_left == 'M' and bottom_right == 'S')
                            or (top_left == 'S' and top_right == 'M' and bottom_left == 'S' and bottom_right == 'M')
                    ):
                        count += 1

    return count


grid = []

while True:
    line = input().strip()
    if not line:
        break
    try:
        grid.append(line)
    except ValueError:
        break

print(counter(grid))
print(counter_x(grid))
