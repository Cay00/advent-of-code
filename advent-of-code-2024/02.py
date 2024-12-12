#   A report only counts as safe if both of the following are true:
#       - The levels are either all increasing or all decreasing.
#       - Any two adjacent levels differ by at least one and at most three.

#   7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
#   1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
#   9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
#   1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
#   8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
#   1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

#   test data:
#   7 6 4 2 1
#   1 2 7 8 9
#   9 7 6 2 1
#   1 3 2 4 5
#   8 6 4 4 1
#   1 3 6 7 9

#   test answer 1: 2
#   test answer 2: 4

def differences(row):
    increasing = None

    for i in range(len(row) - 1):
        difference = abs(row[i] - row[i + 1])
        if not (1 <= difference <= 3):
            return False
        if row[i] < row[i + 1]:
            if increasing is None:
                increasing = True
            elif not increasing:
                return False
        elif row[i] > row[i + 1]:
            if increasing is None:
                increasing = False
            elif increasing:
                return False
    return True


def remover(row):
    if differences(row):
        return True

    for i in range(len(row)):
        new_row = row[:i] + row[i + 1:]
        if differences(new_row):
            return True
    return False


numbers = []

while True:
    line = input().strip()
    if not line:
        break
    try:
        numbers.append([int(num) for num in line.split()])
    except ValueError:
        continue

result = sum(differences(row) for row in numbers)
print(result)

result2 = sum(remover(row) for row in numbers)
print(result2)
