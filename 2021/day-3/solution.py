if __name__ == '__main__':
    file = open("data", "r")
    data = [line.strip() for line in file.readlines()]
    file.close()

    sum = [0] * len(data[0])
    neg_sum = [0] * len(data[0])
    for line in data:
        for i in range(0, len(line)):
            sum[i] += int(line[i])

    for i in range(0, len(sum)):
        if sum[i] > len(data) / 2:
            sum[i] = 1
            neg_sum[i] = 0
        else:
            sum[i] = 0
            neg_sum[i] = 1

    string_sum = "".join([str(integer) for integer in sum])
    string_neg_sum = "".join([str(integer) for integer in neg_sum])

    int_sum = int(string_sum, 2)
    int_neg_sum = int(string_neg_sum, 2)

    print("First part solution: " + str(int_sum * int_neg_sum))

