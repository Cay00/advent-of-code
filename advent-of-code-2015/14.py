def parse_input(text):
    data = {}

    for line in text:
        words = line.split()
        person = words[0]
        speed = int(words[3])
        time = int(words[6])
        rest = int(words[13])
        distance = 0
        points = 0

        data[person] = (speed, time, rest, distance, points)

    return data


def calculate(text):
    data = parse_input(text)
    max_distance = 0
    total_time = 2503  # seconds
    current_leader = None

    for name, (speed, time, rest, distance, points) in data.items():
        cycle_time = time + rest
        distance = 0

        # Total distance
        for i in range(total_time):
            if i % cycle_time < time:
                distance += speed

        # Max distance
        if distance > max_distance:
            max_distance = distance
            current_leader = name

    return current_leader, max_distance


text = []

while True:
    line = input()
    if not line:
        break
    text.append(line)

first = calculate(text)
print(first)
