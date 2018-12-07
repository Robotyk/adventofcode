def setter(table, horizontalDist, verticalDist, width, height):
    for j in range(width):
        for i in range(height):
            table[horizontalDist + i][verticalDist + j] += 1


def checker(table, id, horizontalDist, verticalDist, width, height):
    for j in range(width):
        for i in range(height):
            if table[horizontalDist + i][verticalDist + j] > 1:
                return
    return id


table = [[0 for i in range(1000)] for j in range(1000)]

file_object = open("data", "r")
for x in file_object:
    verticalDist = int(x[(x.find("@") + 2):x.find(",")])
    horizontalDist = int(x[(x.find(",") + 1):x.find(":")])
    width = int(x[(x.find(":") + 2):x.find("x")])
    height = int(x[(x.find("x") + 1):x.__len__()])
    setter(table, horizontalDist, verticalDist, width, height)

counter = 0
for i in range(1000):
    for j in range(1000):
        if table[i][j] > 1:
            counter += 1
print(counter)

file_object = open("data", "r")
for x in file_object:
    id = int(x[(x.find("#") + 1):x.find("@") - 1])
    verticalDist = int(x[(x.find("@") + 2):x.find(",")])
    horizontalDist = int(x[(x.find(",") + 1):x.find(":")])
    width = int(x[(x.find(":") + 2):x.find("x")])
    height = int(x[(x.find("x") + 1):x.__len__()])
    n = checker(table, id, horizontalDist, verticalDist, width, height)
    if n is not None:
        print(n)
        break
