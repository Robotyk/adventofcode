import copy


def simulate_first_rules(data):
    has_changed = True
    while has_changed:
        has_changed = False
        temp = copy.deepcopy(data)
        for i in range(len(data)):
            for j in range(len(data[0])):
                occupied_numbers = 0
                if i > 0 and j > 0 and data[i - 1][j - 1] == "#":
                    occupied_numbers += 1
                if i > 0 and data[i - 1][j] == "#":
                    occupied_numbers += 1
                if i > 0 and j < len(data[0]) - 1 and data[i - 1][j + 1] == "#":
                    occupied_numbers += 1
                if j > 0 and data[i][j - 1] == "#":
                    occupied_numbers += 1
                if j < len(data[0]) - 1 and data[i][j + 1] == "#":
                    occupied_numbers += 1
                if i < len(data) - 1 and j > 0 and data[i + 1][j - 1] == "#":
                    occupied_numbers += 1
                if i < len(data) - 1 and data[i + 1][j] == "#":
                    occupied_numbers += 1
                if i < len(data) - 1 and j < len(data[0]) - 1 and data[i + 1][j + 1] == "#":
                    occupied_numbers += 1

                if data[i][j] == "L" and occupied_numbers == 0:
                    temp[i][j] = "#"
                    has_changed = True
                elif data[i][j] == "#" and occupied_numbers >= 4:
                    temp[i][j] = "L"
                    has_changed = True

        data = temp
    return data


def count_seats(data):
    result, i, j = 0, 0, 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "#":
                result += 1
    return result


def simulate_second_rules(data):
    has_changed = True
    while has_changed:
        has_changed = False
        temp = copy.deepcopy(data)
        for i in range(len(data)):
            for j in range(len(data[0])):
                occupied_numbers = 0
                k, l = i, j
                while k > 0 and l > 0:
                    if data[k - 1][l - 1] == "#":
                        occupied_numbers += 1
                        break
                    if data[k - 1][l - 1] == "L":
                        break
                    k -= 1
                    l -= 1
                k = i
                while k > 0:
                    if data[k - 1][j] == "#":
                        occupied_numbers += 1
                        break
                    if data[k - 1][j] == "L":
                        break
                    k -= 1
                k, l = i, j
                while k > 0 and l < len(data[0]) - 1:
                    if data[k - 1][l + 1] == "#":
                        occupied_numbers += 1
                        break
                    if data[k - 1][l + 1] == "L":
                        break
                    k -= 1
                    l += 1
                l = j
                while l > 0:
                    if data[i][l - 1] == "#":
                        occupied_numbers += 1
                        break
                    if data[i][l - 1] == "L":
                        break
                    l -= 1
                l = j
                while l < len(data[0]) - 1:
                    if data[i][l + 1] == "#":
                        occupied_numbers += 1
                        break
                    if data[i][l + 1] == "L":
                        break
                    l += 1
                k, l = i, j
                while k < len(data) - 1 and l > 0:
                    if data[k + 1][l - 1] == "#":
                        occupied_numbers += 1
                        break
                    if data[k + 1][l - 1] == "L":
                        break
                    k += 1
                    l -= 1
                k = i
                while k < len(data) - 1:
                    if data[k + 1][j] == "#":
                        occupied_numbers += 1
                        break
                    if data[k + 1][j] == "L":
                        break
                    k += 1
                k, l = i, j
                while k < len(data) - 1 and l < len(data[0]) - 1:
                    if data[k + 1][l + 1] == "#":
                        occupied_numbers += 1
                        break
                    if data[k + 1][l + 1] == "L":
                        break
                    k += 1
                    l += 1

                if data[i][j] == "L" and occupied_numbers == 0:
                    temp[i][j] = "#"
                    has_changed = True
                elif data[i][j] == "#" and occupied_numbers >= 5:
                    temp[i][j] = "L"
                    has_changed = True

        data = temp
    return data


if __name__ == '__main__':
    data = []
    with open("day-11-data", "r") as f:
        [data.append(list(line[:-1])) for line in f.readlines()]

    print("First part answer: " + str(count_seats(simulate_first_rules(copy.deepcopy(data)))))
    print("Second part answer: " + str(count_seats(simulate_second_rules(copy.deepcopy(data)))))
