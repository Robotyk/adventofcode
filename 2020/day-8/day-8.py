def find_acc_when_inf_loop():
    previous_instructions = set()
    accumulator, current_position = 0, 0
    while True:
        if current_position in previous_instructions:
            return accumulator
        previous_instructions.add(current_position)
        instruction = data[current_position][:3]
        arg = int(data[current_position][4:])

        if instruction == "jmp":
            current_position += arg
        elif instruction == "acc":
            accumulator += arg
            current_position += 1
        else:
            current_position += 1


def find_wrong_instr():
    for i in range(len(data)):
        new_data = data.copy()
        if "jmp" in new_data[i]:
            new_data[i] = new_data[i].replace("jmp", "nop")
        elif "nop" in new_data[i]:
            new_data[i] = new_data[i].replace("nop", "jmp")
        else:
            continue

        previous_instructions = set()
        accumulator, current_position = 0, 0
        while True:
            if current_position in previous_instructions:
                break
            if current_position == len(new_data):
                return accumulator
            previous_instructions.add(current_position)
            instruction = new_data[current_position][:3]
            arg = int(new_data[current_position][4:])

            if instruction == "jmp":
                current_position += arg
            elif instruction == "acc":
                accumulator += arg
                current_position += 1
            else:
                current_position += 1


if __name__ == '__main__':
    data = []
    with open("day-8-data", "r") as f:
        [data.append(line[:-1]) for line in f.readlines()]

    print("First part answer: " + str(find_acc_when_inf_loop()))
    print("Second part answer: " + str(find_wrong_instr()))
