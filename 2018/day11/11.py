serial_number = 1308


def __calculate_cel_power_lvl(x_axis, y_axis):
    rack_id = x_axis + 10
    power_lvl = ((rack_id * y_axis + serial_number) * rack_id)

    return (power_lvl // 100) % 10 - 5


def calculate_cell_power_field():
    return [[__calculate_cel_power_lvl(x, y) for x in range(300)] for y in range(300)]


def __sum_square(field, x, y):
    return field[x-1][y-1] + field[x][y-1] + field[x+1][y-1] + \
           field[x-1][y]   + field[x][y]   + field[x+1][y] + \
           field[x-1][y+1] + field[x][y+1] + field[x+1][y+1]


def calculate_square_power_field(field):
    return [[__sum_square(field, x + 1, y + 1) for x in range(298)] for y in range(298)]


def find_highest_valued_square(array_of_sum):
    highest_power_square_value = -10
    highest_power_square_location = ""

    for i in range(len(array_of_sum)):
        for j in range(len(array_of_sum[i])):
            if highest_power_square_value < array_of_sum[j][i]:
                highest_power_square_value = array_of_sum[j][i]
                highest_power_square_location = str(j) + ", " + str(i)

    return highest_power_square_location, highest_power_square_value


cel_power_lvl_field = calculate_cell_power_field()
sum_field = calculate_square_power_field(cel_power_lvl_field)

print(find_highest_valued_square(sum_field))