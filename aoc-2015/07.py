def apply_instruction(instructions):
    values = {}

    def get_value(operand, values):
        # If the operand is a number, return its value
        if operand.isdigit():
            return int(operand)
        # If the operand is already in the 'values', return its value
        if operand in values:
            return values[operand]
        return None

    def evaluate_instruction(instruction, values):
        parts = instruction.split()

        if parts[1] == '->':
            value = get_value(parts[0], values)
            if value is not None:
                values[parts[2]] = value
            else:
                return False

        elif parts[1] == "AND":
            a = get_value(parts[0], values)
            b = get_value(parts[2], values)
            if a is not None and b is not None:
                values[parts[4]] = a & b
            else:
                return False

        elif parts[1] == "OR":
            a = get_value(parts[0], values)
            b = get_value(parts[2], values)
            if a is not None and b is not None:
                values[parts[4]] = a | b
            else:
                return False

        elif parts[1] == "LSHIFT":
            a = get_value(parts[0], values)
            shift = int(parts[2])
            if a is not None:
                values[parts[4]] = a << shift
            else:
                return False

        elif parts[1] == "RSHIFT":
            a = get_value(parts[0], values)
            shift = int(parts[2])
            if a is not None:
                values[parts[4]] = a >> shift
            else:
                return False

        elif parts[0] == "NOT":
            a = get_value(parts[1], values)
            if a is not None:
                values[parts[3]] = ~a & 0xFFFF  # Mask to 16-bit value
            else:
                return False

        return True

    # Loop until all values are resolved
    while instructions:
        instruction = instructions.pop(0)
        if not evaluate_instruction(instruction, values):
            # If the instruction could not be processed, add it back to the list for later processing
            instructions.append(instruction)

    return values


instructions = []

while True:
    line = input()
    if not line:
        break
    instructions.append(line)

initial_values = apply_instruction(instructions)
print(initial_values['a'])
