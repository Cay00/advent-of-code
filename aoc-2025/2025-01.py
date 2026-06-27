inputData = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".splitlines()

inputData = [x for x in inputData if x]

position = 50
score = 0

for moves in inputData:
    move = int(moves[1:])

    if moves[0] == "L":
        position = (position - move) % 100
    else:
        position = (position + move) % 100

    if position == 0:
        score += 1

print(score)
