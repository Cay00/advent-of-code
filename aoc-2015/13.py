def parse_input(data):
    happiness = {}
    for line in data:
        words = line.split()
        personA = words[0]
        personB = words[9]
        if words[2] == 'gain':
            change = int(words[3])
        else:
            change = -int(words[3])

        if personA not in happiness:
            happiness[personA] = {}
        happiness[personA][personB] = change

    return happiness


def generate_permutations(people, start=0):
    if start == len(people) - 1:
        return [people[:]]
    permutations = []

    for i in range(start, len(people)):
        people[start], people[i] = people[i], people[start]
        permutations += generate_permutations(people, start + 1)
        people[start], people[i] = people[i], people[start]

    return permutations


def find_optimal(data):
    happiness = parse_input(data)
    people = list(happiness)

    all_arrangements = generate_permutations(people)

    best_happiness = float('-inf')

    return all_arrangements


data = [
    "1 would gain 54 happiness units by sitting next to Bob.",
    "2 would gain 83 happiness units by sitting next to Alice.",
    "3 would lose 62 happiness units by sitting next to Alice.",
]

first = find_optimal(data)
print(first)
