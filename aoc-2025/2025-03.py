inputData = """987654321111111
811111111111119
234234234234278
818181911112111""".splitlines()

score = 0

for item in inputData:
    item = str(item)

    first, second = '0', '0'
    firstIdx = 0

    for i in range(len(item) - 1):
        if item[i] > first:
            first = item[i]
            firstIdx = i

    for i in range(firstIdx + 1, len(item)):
        if item[i] > second:
            second = item[i]

    score += int(first) * 10 + int(second)

print(score)
