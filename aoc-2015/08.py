def coder(text):
    total_len = 0
    letters = 0

    for line in text:
        line = line.strip()
        total_len += len(line)

        i = 1
        while i < len(line) - 1:
            if line[i] == '\\':
                if line[i + 1] == '\\' or line[i + 1] == '"':
                    letters += 1
                    i += 2
                elif line[i + 1] == 'x':  # '\xNN'
                    letters += 1
                    i += 4
            else:
                letters += 1
                i += 1

    return (total_len - letters)


def encoder(text):
    original_size = 0
    new_size = 0

    for line in text:
        letters = 3
        line = line.strip()
        original_size += len(line)

        i = 0
        while i < len(line) - 1:
            if line[i] == '"':
                letters += 3
                i += 1
            elif line[i] == '\\':
                if line[i + 1] == '\\' or line[i + 1] == '"':
                    letters += 4
                    i += 2
                elif line[i + 1] == 'x':  # '\xNN'
                    letters += 2
                    i += 1
            else:
                letters += 1
                i += 1

        new_size += letters

    return (new_size - original_size)


text = []

while True:
    line = input()
    if not line:
        break
    text.append(line)

value = coder(text)
print(value)
value = encoder(text)
print(value)
