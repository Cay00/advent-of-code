def parse_input(text):
    ingredients = {}

    for line in text:
        parts = line.split(': ')
        name = parts[0]
        properties = parts[1].split(", ")
        properties_dict = {}
        for prop in properties:
            key, value = prop.split(" ")
            properties_dict[key] = int(value)
        ingredients[name] = properties_dict

    return ingredients


def calculate(text):
    data = parse_input(text)

    return data


text = [
    "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
    "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"
]

# while True:
#     line = input()
#     if not line:
#         break
#     text.append(line)

answer = calculate(text)
print(answer)
