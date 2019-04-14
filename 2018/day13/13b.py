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
    if len(carts) == 1:
        print("LAST CART POSITION: " + str(carts[0].pos_x) + ", " + str(carts[0].pos_y))
        exit(0)

    carts_to_remove = []
    sorted_carts = sorted(carts, key=lambda k: (k.pos_y, k.pos_x), reverse=False)

    for cart in sorted_carts:
        if cart not in carts_to_remove:
            direction = cart.direction
            if direction == DIRECTION_LEFT:
                x = cart.pos_x
                y = cart.pos_y
                next_field = tracks[y][x - 1]
                tracks[y][x] = cart.previous_sign

                if next_field == "-":
                    tracks[y][x - 1] = DIRECTION_LEFT
                    cart.pos_x = x - 1
                    cart.previous_sign = "-"
                elif next_field == "\\":
                    tracks[y][x - 1] = DIRECTION_UP
                    cart.pos_x = x - 1
                    cart.direction = DIRECTION_UP
                    cart.previous_sign = "\\"
                elif next_field == "/":
                    tracks[y][x - 1] = DIRECTION_DOWN
                    cart.pos_x = x - 1
                    cart.direction = DIRECTION_DOWN
                    cart.previous_sign = "/"
                elif next_field == "+":
                    cart.pos_x = x - 1
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
                    carts_to_remove.append(cart)
                    for i in carts:
                        if i.pos_x == x - 1 and i.pos_y == y:
                            tracks[i.pos_y][i.pos_x] = i.previous_sign
                            carts_to_remove.append(i)
                else:
                    print("ERROR - unknown next field: " + str(next_field))

            elif direction == DIRECTION_RIGHT:

                x = cart.pos_x
                y = cart.pos_y
                next_field = tracks[y][x + 1]
                tracks[y][x] = cart.previous_sign

                if next_field == "-":
                    tracks[y][x + 1] = DIRECTION_RIGHT
                    cart.pos_x = x + 1
                    cart.previous_sign = "-"
                elif next_field == "\\":
                    tracks[y][x + 1] = DIRECTION_DOWN
                    cart.pos_x = x + 1
                    cart.direction = DIRECTION_DOWN
                    cart.previous_sign = "\\"
                elif next_field == "/":
                    tracks[y][x + 1] = DIRECTION_UP
                    cart.pos_x = x + 1
                    cart.direction = DIRECTION_UP
                    cart.previous_sign = "/"
                elif next_field == "+":
                    cart.pos_x = x + 1
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
                    carts_to_remove.append(cart)
                    for i in carts:
                        if i.pos_x == x + 1 and i.pos_y == y:
                            tracks[i.pos_y][i.pos_x] = i.previous_sign
                            carts_to_remove.append(i)
                else:
                    print("ERROR - unknown next field: " + str(next_field))

            elif direction == DIRECTION_UP:

                x = cart.pos_x
                y = cart.pos_y
                next_field = tracks[y - 1][x]
                tracks[y][x] = cart.previous_sign

                if next_field == "|":
                    tracks[y - 1][x] = DIRECTION_UP
                    cart.pos_y = y - 1
                    cart.previous_sign = "|"
                elif next_field == "\\":
                    tracks[y - 1][x] = DIRECTION_LEFT
                    cart.pos_y = y - 1
                    cart.direction = DIRECTION_LEFT
                    cart.previous_sign = "\\"
                elif next_field == "/":
                    tracks[y - 1][x] = DIRECTION_RIGHT
                    cart.pos_y = y - 1
                    cart.direction = DIRECTION_RIGHT
                    cart.previous_sign = "/"
                elif next_field == "+":
                    cart.pos_y = y - 1
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
                    carts_to_remove.append(cart)
                    for i in carts:
                        if i.pos_x == x and i.pos_y == y - 1:
                            tracks[i.pos_y][i.pos_x] = i.previous_sign
                            carts_to_remove.append(i)
                else:
                    print("ERROR - unknown next field: " + str(next_field))

            elif direction == DIRECTION_DOWN:

                x = cart.pos_x
                y = cart.pos_y
                next_field = tracks[y + 1][x]
                tracks[y][x] = cart.previous_sign

                if next_field == "|":
                    cart.pos_y = y + 1
                    tracks[y + 1][x] = DIRECTION_DOWN
                    cart.previous_sign = "|"
                elif next_field == "\\":
                    tracks[y + 1][x] = DIRECTION_RIGHT
                    cart.pos_y = y + 1
                    cart.direction = DIRECTION_RIGHT
                    cart.previous_sign = "\\"
                elif next_field == "/":
                    tracks[y + 1][x] = DIRECTION_LEFT
                    cart.pos_y = y + 1
                    cart.direction = DIRECTION_LEFT
                    cart.previous_sign = "/"
                elif next_field == "+":
                    cart.pos_y = y + 1
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
                    carts_to_remove.append(cart)
                    for i in carts:
                        if i.pos_x == x and i.pos_y == y + 1:
                            tracks[i.pos_y][i.pos_x] = i.previous_sign
                            carts_to_remove.append(i)
                else:
                    print("ERROR - unknown next field: " + str(next_field))
            else:
                print("ERROR - unknown direction: " + direction)

    for c in set(carts_to_remove):
        carts.remove(c)
