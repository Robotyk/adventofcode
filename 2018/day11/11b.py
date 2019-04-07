serial_number = 1308


def __calculate_cel_power_lvl(x_axis, y_axis):
    rack_id = x_axis + 10
    power_lvl = ((rack_id * y_axis + serial_number) * rack_id)

    return (power_lvl // 100) % 10 - 5


def calculate_cell_power_field():
    return [[__calculate_cel_power_lvl(x, y) for x in range(300)] for y in range(300)]


def find_biggest_score(field):
    current_highest_sum = 0
    for size in range(1, 20):
        for l in range(len(field) - size):
            for k in range(len(field) - size):
                sum = 0
                for i in range(size):
                    for j in range(size):
                        sum += field[k + j][l + i]
                if sum > current_highest_sum:
                    current_highest_sum = sum
                    highest_sum_details = (l, k, size)

    return current_highest_sum, highest_sum_details


cel_power_lvl_field = calculate_cell_power_field()
print(find_biggest_score(cel_power_lvl_field))
