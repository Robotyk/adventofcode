def find_my_seat_id():
    mid, i = 64, 0
    while True:
        for seat in free_seats:
            if seat[0] == mid + i:
                return str(seat[0] * 8 + seat[1])
        i += 1



if __name__ == '__main__':
    file = open("day-5-data", "r")
    table = {70: 48, 66: 49, 82: 49, 76: 48}
    seats = []
    for line in file.readlines():
        row = int(line[:-4].translate(table), 2)
        column = int(line[-4:].translate(table), 2)
        seats.append((row, column))

    print("First part answer: " + str(max([x[0] * 8 + x[1] for x in seats])))

    all_seats = []
    for i in range(128):
        for j in range(8):
            all_seats.append((i, j))

    free_seats = [x for x in all_seats if x not in seats]

    print("Second part answer: " + find_my_seat_id())

