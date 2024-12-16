def apply_instruction(instructions):
    grid = [[0] * 1000 for _ in range(1000)]
    grid_bright = [[0] * 1000 for _ in range(1000)]

    for instruction in instructions:
        parts = instruction.split()

        if parts[0] == "turn":
            x1, y1 = map(int, parts[2].split(','))
            x2, y2 = map(int, parts[4].split(','))

            if parts[1] == "on":
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        grid[x][y] = 1
                        grid_bright[x][y] += 1
            elif parts[1] == "off":
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        grid[x][y] = 0
                        if grid_bright[x][y] > 0:
                            grid_bright[x][y] -= 1

        elif parts[0] == "toggle":
            x1, y1 = map(int, parts[1].split(','))
            x2, y2 = map(int, parts[3].split(','))

            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid[x][y] = 1 - grid[x][y]
                    grid_bright[x][y] += 2

    lights = sum(sum(row) for row in grid)
    brightness = sum(sum(row) for row in grid_bright)

    return lights, brightness


instructions = []

while True:
    line = input()
    if not line:
        break
    instructions.append(line)

print(apply_instruction(instructions))
