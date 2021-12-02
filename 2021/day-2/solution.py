if __name__ == '__main__':
    file = open("data", "r")
    data = [(line.split()[0], int(line.split()[1])) for line in file.readlines()]
    file.close()

    horizontal_position, depth = 0, 0

    for move in data:
        if move[0] == "forward":
            horizontal_position += move[1]
        if move[0] == "up":
            depth -= move[1]
        if move[0] == "down":
            depth += move[1]

    print("First part solution: " + str(horizontal_position * depth))

    horizontal_position, depth, aim = 0, 0, 0

    for move in data:
        if move[0] == "forward":
            horizontal_position += move[1]
            depth += aim * move[1]
        if move[0] == "up":
            aim -= move[1]
        if move[0] == "down":
            aim += move[1]

    print("Second part solution: " + str(horizontal_position * depth))
