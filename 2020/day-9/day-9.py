def find_invalid_number():
    i = 25
    while i < len(data):
        if not is_sum_of_previous(i):
            return data[i]
        i += 1


def is_sum_of_previous(line_number):
    for i in range(line_number - 25, line_number - 1):
        for j in range(i + 1, line_number):
            if data[i] + data[j] == data[line_number]:
                return True
    return False


def find_summands_list(invalid_number):
    for i in range(len(data) - 1):
        sum = 0
        for j in range(i, len(data)):
            sum += data[j]
            if sum == invalid_number:
                return min(data[i:j]) + max(data[i:j])
            if sum > invalid_number:
                break


if __name__ == '__main__':
    data = []
    with open("day-9-data", "r") as f:
        [data.append(int(line[:-1])) for line in f.readlines()]

    invalid_number = find_invalid_number()
    print("First part answer: " + str(invalid_number))
    print("Second part answer: " + str(find_summands_list(invalid_number)))





