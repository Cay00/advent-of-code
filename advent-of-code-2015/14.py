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
    max_points = 0
    total_time = 2503  # seconds

    for i in range(total_time):
        max_distance = 0
        for name, (speed, time, rest, distance, points) in data.items():
            # Total distance
            if i % (time + rest) < time:
                distance += speed
            # Max distance
            if distance > max_distance:
                max_distance = distance
            data[name] = (speed, time, rest, distance, points)

        for name, (speed, time, rest, distance, points) in data.items():
            if distance >= max_distance:
                points += 1
                if points > max_points:
                    max_points = points
            data[name] = (speed, time, rest, distance, points)

    return max_distance, max_points


text = []

while True:
    line = input()
    if not line:
        break
    text.append(line)

first = calculate(text)
print(first)
