#   the goal of the program is just to multiply some numbers.
#   It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers.
#   For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024.
#   Similarly, mul(123,4) would multiply 123 by 4.
#
#   However, because the program's memory has been corrupted,
#   there are also many invalid characters that should be ignored,
#   even if they look like part of a mul instruction.
#   Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

#   test data 1:
#   xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

#   test data 2:
#   xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))

#   test answer 1: 161
#   test answer 2: 48

import re


def multilpier(text):
    result = 0
    pattern = r'mul\((\d+),(\d+)\)'
    #   'mul(' + decimals + ',' + deimals + ')'
    matches = re.findall(pattern, text)

    if matches:
        for match in matches:
            number1 = int(match[0])  # Pierwsza liczba
            number2 = int(match[1])  # Druga liczba
            result += (number1 * number2)
    return result


def multilpier2(text):
    mul = True
    total = 0

    #   match do(), don't(), and mul(X,Y) instructions, and ignore others.
    instructions = re.findall(r"do\(\)|don't\(\)|mul\(\d+\s*,\s*\d+\)", text)
    for instruction in instructions:
        if instruction == "do()":
            mul = True  # Włącz mnożenie
        elif instruction == "don't()":
            mul = False  # Wyłącz mnożenie
        elif mul and instruction.startswith("mul("):
            match = re.match(r"mul\((\d+),\s*(\d+)\)", instruction)
            if match:
                num1, num2 = map(int, match.groups())
                total += num1 * num2  # Dodajemy wynik mnożenia do s

    return total


while True:
    text = ""
    while True:
        line = input()
        if line == "":
            break
        text += line + "\n"

    print(multilpier(text))
    print(multilpier2(text))
