with open("data", "r") as file:
    line = file.readline().split()

data = list(map(int, line))


class Node:
    def __init__(self):
        self.number_of_children = 0
        self.number_of_metadata = 0
        self.children = []
        self.metadata = []


def prepare_data(i):
    if data and data[i] == 0:
        node = Node()
        node.number_of_metadata = data[i + 1]
        for j in range(i + 2, i + 2 + data[i + 1]):
            node.metadata.append(data[i + 2])
            data.pop(i + 2)
        data.pop(i)
        data.pop(i)
        return node
    else:
        node = Node()
        node.number_of_children = data[i]
        node.number_of_metadata = data[i + 1]
        for j in range(0, data[i]):
            node.children.append(prepare_data(i + 2))
        for j in range(i + 2, i + 2 + data[i + 1]):
            node.metadata.append(data[i + 2])
            data.pop(i + 2)
        data.pop(i)
        data.pop(i)
        return node


root = prepare_data(0)


