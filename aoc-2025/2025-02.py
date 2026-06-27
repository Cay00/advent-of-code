inputData = """95-115""".split(',')

score = 0

for item in inputData:
    left, right = item.split('-')

    for number in range(int(left), int(right) + 1):
        if len(str(number)) % 2 == 0:
            half = len(str(number)) // 2
            number = str(number)
            if number[half:] == number[:half]:
                score += int(number)
print(score)
