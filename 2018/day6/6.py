def get_boundaries():
    top = 999
    bot = 0
    left = 999
    right = 0
    file_object = open("data", "r")
    for line in file_object:
        x_axis = int(line[:line.find(",")])
        y_axis = int(line[line.find(",") + 1:])
        if x_axis < left:
            left = x_axis
        if x_axis > right:
            right = x_axis
        if y_axis < top:
            top = y_axis
        if y_axis > bot:
            bot = y_axis
    return left, right, top, bot


def init_dict():
    empty_dictionary = {}
    for i in range(boundaries[0], boundaries[1] + 1):
        for j in range(boundaries[2], boundaries[3] + 1):
            empty_dictionary[str(i) + ":" + str(j)] = 999
    return empty_dictionary


def calculate_dist(x_a, y_a, x_b, y_b):
    return abs(x_b - x_a) + abs(y_b - y_a)


boundaries = get_boundaries()
distances = init_dict()
file_object = open("data", "r")
distances2 = {}
same_distances = {}
for line in file_object:
    for i in range(boundaries[0], boundaries[1] + 1):
        for j in range(boundaries[2], boundaries[3] + 1):
            x_from_line = int(line[:line.find(",")])
            y_from_line = int(line[line.find(",") + 1:])
            current_distance = calculate_dist(i, j, x_from_line, y_from_line)
            dictionary_key = str(i) + ":" + str(j)
            if distances.get(dictionary_key) > current_distance:
                distances[dictionary_key] = current_distance
                distances2[dictionary_key] = (line[:line.find(",")]) + ":" + line[line.find(",") + 2:-1]
            elif distances.get(dictionary_key) == current_distance:
                same_distances[dictionary_key] = current_distance

counter_storage = {}
black_list = set()
for x in distances2:
    if x in same_distances and distances2.get(x) == same_distances.get(x):
        continue
    if str(boundaries[0]) in x[:x.find(":")] or str(boundaries[1]) in x[:x.find(":")] or str(boundaries[2]) in x[x.find(":") + 1:] or str(boundaries[3]) in x[x.find(":") + 1:]:
        black_list.add(distances2.get(x))
    if distances2.get(x) not in counter_storage:
        counter_storage[distances2.get(x)] = 1
    else:
        counter_storage[distances2.get(x)] = counter_storage.get(distances2.get(x)) + 1

max = 0
for x in counter_storage:
    if max < counter_storage.get(x) and x not in black_list:
        max = counter_storage.get(x)
print(max)