#   test data:
#   3 4
#   4 3
#   2 5
#   1 3
#   3 9
#   3 3
#
#   test answer: 11

column1 = []
column2 = []

while True:
    try:
        row = input()
        if not row:
            break
        numbers = tuple(map(int, row.split()))
        column1.append(numbers[0])
        column2.append(numbers[1])
    except ValueError:
        continue

column1 = sorted(column1)
column2 = sorted(column2)

distance = sum(abs(a - b) for a, b in zip(column1, column2))

print(distance)
