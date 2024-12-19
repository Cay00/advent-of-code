def parse_input(text):
    data = {}

    for line in text:
        words = line.split()
        person = words[0]
        speed = int(words[3])
        time = int(words[6])
        rest = int(words[13])
        distance = 0

        data[person] = (speed, time, rest, distance)

    return data


def calculate(text):
    data = parse_input(text)
    max = 0
    total_time = 2503  # seconds

    for name, (speed, time, rest, distance) in data.items():
        cycle_time = time + rest
        # cycle = 0

        for i in range(total_time):
            if (i) % cycle_time < time:
                distance += speed
            # if (i) % cycle_time == 0:
            #     cycle += 1

        if distance > max:
            max = distance
        #print(name, distance)

    return max


text = []

while True:
    line = input()
    if not line:
        break
    text.append(line)

first = calculate(text)
print(first)
