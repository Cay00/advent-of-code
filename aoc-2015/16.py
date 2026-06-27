def parse_input(text):
    aunts = {}

    for line in text:
        parts = line.split(": ", 1)
        name = parts[0]
        attributes = parts[1].split(", ")

        attributes_dict = {}
        for prop in attributes:
            key, value = prop.split(": ")
            attributes_dict[key] = int(value)

        aunts[name] = attributes_dict

    return aunts


def analyse(text):
    data = parse_input(text)

    for sue, properties in data.items():
        matches = 0

        for prop, value in properties.items():
            if prop in mfcsam_results and value != mfcsam_results[prop]:
                break
            elif prop in mfcsam_results and value == mfcsam_results[prop]:
                matches += 1

        if matches == 3:
            return sue
    return None


def analyse_2(text):
    data = parse_input(text)

    for sue, properties in data.items():
        match = True

        for prop, value in properties.items():
            if prop in mfcsam_results:
                if prop in {'cats', 'trees'}:
                    if value <= mfcsam_results[prop]:
                        match = False
                        break
                elif prop in {'pomeranians', 'goldfish'}:
                    if value >= mfcsam_results[prop]:
                        match = False
                        break
                else:
                    if value != mfcsam_results[prop]:
                        match = False
                        break
        if match:
            return sue

    return None


mfcsam_results = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

text = []

while True:
    line = input()
    if not line:
        break
    text.append(line)

answer = analyse(text)
print(answer)
answer = analyse_2(text)
print(answer)
