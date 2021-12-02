if __name__ == '__main__':
    memory = {}
    with open("day-14-data", "r") as f:
        for line in f.readlines():
            if "mask" in line:
                current_mask = line[7:-1]
                set_mask = int(current_mask.translate(current_mask.maketrans("X", "0")), 2)
                unset_mask = int(current_mask.translate(current_mask.maketrans("X", "1")), 2)
            else:
                key = line[line.index("[") + 1:line.index("]")]
                value = (int(line[line.index("=") + 2:]))
                memory[key] = (value | set_mask) & unset_mask

    print("First part answer: " + str(sum(memory.values())))

