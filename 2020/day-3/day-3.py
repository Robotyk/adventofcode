def count_trees(data, right_step_size, down_step_size):
    line_length = len(data[0]) - 1
    current_position, counter = 0, 0
    for line in data[down_step_size::down_step_size]:
        current_position = current_position + right_step_size
        if line[current_position % line_length] == "#":
            counter += 1
    return counter


if __name__ == '__main__':
    file = open("day-3-data", "r")
    data = []
    [data.append(line) for line in file.readlines()]

    print("First part answer: " + str(count_trees(data, 3, 1)))
    print("Second part answer: " + str(count_trees(data, 1, 1) * count_trees(data, 3, 1) * count_trees(data, 5, 1) * count_trees(data, 7, 1) * count_trees(data, 1, 2)))

    file.close()
