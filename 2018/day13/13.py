DIRECTION_LEFT = "<"
DIRECTION_RIGHT = ">"
DIRECTION_DOWN = "v"
DIRECTION_UP = "^"

RIGHT = "right"
LEFT = "left"
STRAIGHT = "straight"


class Cart:
    def __init__(self, x, y, direction, previous_sign):
        self.pos_x = x
        self.pos_y = y
        self.direction = direction
        self.previous_turn = RIGHT
        self.previous_sign = previous_sign


tracks = []
carts = []


with open("data", "r") as file:
    for line in file:
        tracks.append(list(line))


for y in range(len(tracks)):
    for x in range(len(tracks[y])):
        if tracks[y][x] == DIRECTION_LEFT or tracks[y][x] == DIRECTION_RIGHT:
            carts.append(Cart(x, y, tracks[y][x], "-"))
        elif tracks[y][x] == DIRECTION_UP or tracks[y][x] == DIRECTION_DOWN:
            carts.append(Cart(x, y, tracks[y][x], "|"))

while True:
    for cart in sorted(carts, key=lambda k: (k.pos_y, k.pos_x), reverse=False):
        direction = cart.direction
        if direction == DIRECTION_LEFT:
            x = cart.pos_x
            y = cart.pos_y
            next_field = tracks[y][x - 1]
            tracks[y][x] = cart.previous_sign
            cart.pos_x = x - 1

            if next_field == "-":
                tracks[y][x - 1] = DIRECTION_LEFT
                cart.previous_sign = "-"
            elif next_field == "\\":
                tracks[y][x - 1] = DIRECTION_UP
                cart.direction = DIRECTION_UP
                cart.previous_sign = "\\"
            elif next_field == "/":
                tracks[y][x - 1] = DIRECTION_DOWN
                cart.direction = DIRECTION_DOWN
                cart.previous_sign = "/"
            elif next_field == "+":
                if cart.previous_turn == RIGHT:
                    tracks[y][x - 1] = DIRECTION_DOWN
                    cart.direction = DIRECTION_DOWN
                    cart.previous_turn = LEFT
                elif cart.previous_turn == LEFT:
                    tracks[y][x - 1] = DIRECTION_LEFT
                    cart.previous_turn = STRAIGHT
                elif cart.previous_turn == STRAIGHT:
                    tracks[y][x - 1] = DIRECTION_UP
                    cart.direction = DIRECTION_UP
                    cart.previous_turn = RIGHT
                else:
                    print("ERROR - unknown previous turn: " + cart.previous_turn)
                cart.previous_sign = "+"
            elif next_field == DIRECTION_UP or next_field == DIRECTION_DOWN or next_field == DIRECTION_LEFT or next_field == DIRECTION_RIGHT:
                print("COLLISION DETECTED FIELDS: " + str(x - 1) +  ", " + str(y))
                exit(0)
            else:
                print("ERROR - unknown next field: " + str(next_field))

        elif direction == DIRECTION_RIGHT:

            x = cart.pos_x
            y = cart.pos_y
            next_field = tracks[y][x + 1]
            tracks[y][x] = cart.previous_sign
            cart.pos_x = x + 1

            if next_field == "-":
                tracks[y][x + 1] = DIRECTION_RIGHT
                cart.previous_sign = "-"
            elif next_field == "\\":
                tracks[y][x + 1] = DIRECTION_DOWN
                cart.direction = DIRECTION_DOWN
                cart.previous_sign = "\\"
            elif next_field == "/":
                tracks[y][x + 1] = DIRECTION_UP
                cart.direction = DIRECTION_UP
                cart.previous_sign = "/"
            elif next_field == "+":
                if cart.previous_turn == RIGHT:
                    tracks[y][x + 1] = DIRECTION_UP
                    cart.direction = DIRECTION_UP
                    cart.previous_turn = LEFT
                elif cart.previous_turn == LEFT:
                    tracks[y][x + 1] = DIRECTION_RIGHT
                    cart.previous_turn = STRAIGHT
                elif cart.previous_turn == STRAIGHT:
                    tracks[y][x + 1] = DIRECTION_DOWN
                    cart.direction = DIRECTION_DOWN
                    cart.previous_turn = RIGHT
                else:
                    print("ERROR - unknown previous turn: " + cart.previous_turn)
                cart.previous_sign = "+"
            elif next_field == DIRECTION_UP or next_field == DIRECTION_DOWN or next_field == DIRECTION_LEFT or next_field == DIRECTION_RIGHT:
                print("COLLISION DETECTED FIELDS: " + str(x + 1) +  ", " + str(y))
                exit(0)
            else:
                print("ERROR - unknown next field: " + str(next_field))

        elif direction == DIRECTION_UP:

            x = cart.pos_x
            y = cart.pos_y
            next_field = tracks[y - 1][x]
            tracks[y][x] = cart.previous_sign
            cart.pos_y = y - 1

            if next_field == "|":
                tracks[y - 1][x] = DIRECTION_UP
                cart.previous_sign = "|"
            elif next_field == "\\":
                tracks[y - 1][x] = DIRECTION_LEFT
                cart.direction = DIRECTION_LEFT
                cart.previous_sign = "\\"
            elif next_field == "/":
                tracks[y - 1][x] = DIRECTION_RIGHT
                cart.direction = DIRECTION_RIGHT
                cart.previous_sign = "/"
            elif next_field == "+":
                if cart.previous_turn == RIGHT:
                    tracks[y - 1][x] = DIRECTION_LEFT
                    cart.direction = DIRECTION_LEFT
                    cart.previous_turn = LEFT
                elif cart.previous_turn == LEFT:
                    tracks[y - 1][x] = DIRECTION_UP
                    cart.previous_turn = STRAIGHT
                elif cart.previous_turn == STRAIGHT:
                    tracks[y - 1][x] = DIRECTION_RIGHT
                    cart.direction = DIRECTION_RIGHT
                    cart.previous_turn = RIGHT
                else:
                    print("ERROR - unknown previous turn: " + cart.previous_turn)
                cart.previous_sign = "+"
            elif next_field == DIRECTION_UP or next_field == DIRECTION_DOWN or next_field == DIRECTION_LEFT or next_field == DIRECTION_RIGHT:
                print("COLLISION DETECTED FIELDS: " + str(x) +  ", " + str(y - 1))
                exit(0)
            else:
                print("ERROR - unknown next field: " + str(next_field))

        elif direction == DIRECTION_DOWN:

            x = cart.pos_x
            y = cart.pos_y
            next_field = tracks[y + 1][x]
            tracks[y][x] = cart.previous_sign
            cart.pos_y = y + 1

            if next_field == "|":
                tracks[y + 1][x] = DIRECTION_DOWN
                cart.previous_sign = "|"
            elif next_field == "\\":
                tracks[y + 1][x] = DIRECTION_RIGHT
                cart.direction = DIRECTION_RIGHT
                cart.previous_sign = "\\"
            elif next_field == "/":
                tracks[y + 1][x] = DIRECTION_LEFT
                cart.direction = DIRECTION_LEFT
                cart.previous_sign = "/"
            elif next_field == "+":
                if cart.previous_turn == RIGHT:
                    tracks[y + 1][x] = DIRECTION_RIGHT
                    cart.direction = DIRECTION_RIGHT
                    cart.previous_turn = LEFT
                elif cart.previous_turn == LEFT:
                    tracks[y + 1][x] = DIRECTION_DOWN
                    cart.previous_turn = STRAIGHT
                elif cart.previous_turn == STRAIGHT:
                    tracks[y + 1][x] = DIRECTION_LEFT
                    cart.direction = DIRECTION_LEFT
                    cart.previous_turn = RIGHT
                else:
                    print("ERROR - unknown previous turn: " + cart.previous_turn)
                cart.previous_sign = "+"
            elif next_field == DIRECTION_UP or next_field == DIRECTION_DOWN or next_field == DIRECTION_LEFT or next_field == DIRECTION_RIGHT:
                print("COLLISION DETECTED FIELDS: " + str(x) + ", " + str(y + 1))
                exit(0)
            else:
                print("ERROR - unknown next field: " + str(next_field))
        else:
            print("ERROR - unknown direction: " + direction)