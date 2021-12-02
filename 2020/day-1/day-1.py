def find_two_summands(data):
    x_1, x_2 = 0, 1
    while x_1 < len(data):
        while data[x_1] + data[x_2] <= 2020:
            if data[x_1] + data[x_2] == 2020:
                return data[x_1] * data[x_2]
            x_2 += 1
        x_1 += 1
        x_2 = x_1 + 1


def find_three_summands(data):
    x_1, x_2, x_3 = 0, 1, 2
    while x_1 < len(data):
        while data[x_1] + data[x_2] + data[x_3] <= 2020:
            while data[x_1] + data[x_2] + data[x_3] <= 2020:
                if data[x_1] + data[x_2] + data[x_3] == 2020:
                    return data[x_1] * data[x_2] * data[x_3]
                x_3 += 1
            x_2 += 1
            x_3 = x_2 + 1
        x_1 += 1
        x_2 = x_1 + 1


if __name__ == '__main__':
    file = open("day-1/day-1-data", "r")
    data = list(map(int, file.readlines()))
    data.sort()

    print("first answer: " + str(find_two_summands(data)))
    print("second answer: " + str(find_three_summands(data)))

    file.close()
