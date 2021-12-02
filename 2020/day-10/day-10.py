def count_one_and_three_diff():
    one_jolt_diff, three_jolt_diff = 0, 1
    if data[0] == 1:
        one_jolt_diff += 1
    if data[0] == 3:
        three_jolt_diff += 1
    for i in range(len(data) - 1):
        if data[i + 1] - data[i] == 1:
            one_jolt_diff += 1
        if data[i + 1] - data[i] == 3:
            three_jolt_diff += 1

    return one_jolt_diff, three_jolt_diff


class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children


def build_nodes():
    nodes = []
    i = 0
    while i < len(data) - 1:
        children = []
        if i < len(data) - 1 and data[i + 1] - data[i] <= 3:
            children.append(Node(data[i + 1], []))
        if i < len(data) - 2 and data[i + 2] - data[i] <= 3:
            children.append(Node(data[i + 2], []))
        if i < len(data) - 3 and data[i + 3] - data[i] <= 3:
            children.append(Node(data[i + 3], []))
        if len(children) > 1:
            nodes.append(Node(data[i], children))
        i += 1

    return nodes


def connect_nodes_into_trees():
    trees = []
    i = len(nodes) - 1
    while i >= 0:
        is_unique = True
        for node in nodes:
            for child in node.children:
                if nodes[i].value == child.value:
                    is_unique = False
                    child.children.extend(nodes[i].children)

        if is_unique:
            trees.append(nodes[i])

        i -= 1
    return trees


def count_paths(root, counter=0):
    if len(root.children) == 0:
        return counter + 1
    for child in root.children:
        counter = count_paths(child, counter)
    return counter


if __name__ == '__main__':
    data = []
    with open("day-10-data", "r") as f:
        [data.append(int(line[:-1])) for line in f.readlines()]
    data.sort()

    print("First part answer: " + str(count_one_and_three_diff()[0] * count_one_and_three_diff()[1]))

    data.insert(0, 0)
    data.append(data[len(data) - 1] + 3)
    nodes = build_nodes()
    trees = connect_nodes_into_trees()
    routes_quantity = 1
    for x in trees:
        routes_quantity *= count_paths(x)

    print("Second part answer: " + str(routes_quantity))
