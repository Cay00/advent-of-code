#   Find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l.
#   The elves also need a little extra paper for each present: the area of the smallest side.
#   How many total square feet of wrapping paper should they order?

def multiplier(numbers):
    # Input l, w, h
    l = numbers[0]
    w = numbers[1]
    h = numbers[2]

    lw = l * w
    wh = w * h
    hl = l * h

    smallest_side = min(lw, wh, hl)
    total_area = 2 * lw + 2 * wh + 2 * hl + smallest_side

    return total_area


def ribbon(numbers):
    total_length = numbers[0] * numbers[1] * numbers[2]

    numbers.sort()
    total_length += 2 * numbers[0] + 2 * numbers[1]

    return total_length


total_paper = 0
total_ribbon = 0

while True:
    line = input()
    if not line:
        break
    l, w, h = map(int, line.split('x'))
    numbers = [l, w, h]
    total_paper += multiplier(numbers)
    total_ribbon += ribbon(numbers)

print(total_paper)
print(total_ribbon)
