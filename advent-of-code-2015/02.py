#   Find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l.
#   The elves also need a little extra paper for each present: the area of the smallest side.
#   How many total square feet of wrapping paper should they order?

def multiplier(l, w, h):
    # Input l, w, h
    lw = l * w
    wh = w * h
    hl = l * h

    smallest_side = min(lw, wh, hl)
    total_area = 2 * lw + 2 * wh + 2 * hl + smallest_side

    return total_area


total = 0

while True:
    line = input()
    if not line:
        break
    l, w, h = map(int, line.split('x'))
    total += multiplier(l, w, h)

print(total)
