class Point:
    def __init__(self, pos_x, pos_y, vel_x, vel_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y


points = []

with open("data", "r") as file:
    for line in file:
        position_x = int(line[10:16])
        position_y = int(line[18:24])
        velocity_x = int(line[36:38])
        velocity_y = int(line[40:42])

        points.append(Point(position_x, position_y, velocity_x, velocity_y))


def move():
    for i in points:
        i.pos_x = i.pos_x + i.vel_x
        i.pos_y = i.pos_y + i.vel_y


def check_position(seconds):
    abc = {}
    for i in points:
        abc[i.pos_x] = abc.get(i.pos_x, 0) + 1
    if max(abc.values()) > 20:
        print("Seconds passed: " + str(seconds))
        range = get_range()
        save_result(range[0], range[1], range[2], range[3])


def get_range():
    max_range_x = -50000
    min_range_x = 50000
    max_range_y = -50000
    min_range_y = 50000

    for i in points:
        if i.pos_x > max_range_x:
            max_range_x = i.pos_x
        if i.pos_x < min_range_x:
            min_range_x = i.pos_x

        if i.pos_y > max_range_y:
            max_range_y = i.pos_y
        if i.pos_y < min_range_y:
            min_range_y = i.pos_y

    return max_range_x, min_range_x, max_range_y, min_range_y


def save_result(max_range_x, min_range_x, max_range_y, min_range_y):
    sky = [[" " for x in range(min_range_x, max_range_x + 1)] for y in range(min_range_y, max_range_y + 1)]
    for i in points:
        sky[(i.pos_y - min_range_y)][(i.pos_x - min_range_x)] = "#"

    for i in sky:
        for j in i:
            print(j + " ", end="")
        print("")
    exit(0)


seconds = 0
while True:
    check_position(seconds)
    move()
    seconds += 1
