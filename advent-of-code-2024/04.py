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
