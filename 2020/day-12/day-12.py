def calculate_position():
    x_pos, y_pos, direction = 0, 0, 90
    for instr in data:
        if instr[0] == "N" or (instr[0] == "F" and direction == 0):
            y_pos += instr[1]
        elif instr[0] == "S" or (instr[0] == "F" and direction == 180):
            y_pos -= instr[1]
        elif instr[0] == "E" or (instr[0] == "F" and direction == 90):
            x_pos += instr[1]
        elif instr[0] == "W" or (instr[0] == "F" and direction == 270):
            x_pos -= instr[1]
        elif instr[0] == "R":
            direction = (direction + instr[1]) % 360
        elif instr[0] == "L":
            direction = (direction - instr[1]) % 360
    return x_pos, y_pos


def calculate_position_via_waypoint():
    ship_x_pos, ship_y_pos, wp_x_pos, wp_y_pos = 0, 0, 10, 1
    for instr in data:
        if instr[0] == "N":
            wp_y_pos += instr[1]
        elif instr[0] == "S":
            wp_y_pos -= instr[1]
        elif instr[0] == "E":
            wp_x_pos += instr[1]
        elif instr[0] == "W":
            wp_x_pos -= instr[1]
        elif instr[0] == "F":
            ship_x_pos += wp_x_pos * instr[1]
            ship_y_pos += wp_y_pos * instr[1]
        elif (instr[0] == "R" and instr[1] == 90) or (instr[0] == "L" and instr[1] == 270):
            temp_wp_x_pos = wp_x_pos
            wp_x_pos = wp_y_pos
            wp_y_pos = - temp_wp_x_pos
        elif (instr[0] == "R" and instr[1] == 270) or (instr[0] == "L" and instr[1] == 90):
            temp_wp_x_pos = wp_x_pos
            wp_x_pos = - wp_y_pos
            wp_y_pos = temp_wp_x_pos
        else:
            wp_x_pos = - wp_x_pos
            wp_y_pos = - wp_y_pos
    return ship_x_pos, ship_y_pos


if __name__ == '__main__':
    data = []
    with open("day-12-data", "r") as f:
        [data.append((line[:1], int(line[1:-1]))) for line in f.readlines()]

    print("First part answer: " + str(abs(calculate_position()[0]) + abs(calculate_position()[1])))
    print("First part answer: " + str(abs(calculate_position_via_waypoint()[0]) + abs(calculate_position_via_waypoint()[1])))