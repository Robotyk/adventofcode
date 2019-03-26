nodes_with_predecessors = {}
nodes_with_successor = {}
visited_nodes = set()
nodes_to_visit = []

file = open("data", "r")
for line in file:
    line = line.split()
    previous_node = line[1]
    next_node = line[-3]

    if previous_node in nodes_with_successor:
        nodes_with_successor[previous_node].append(next_node)
    else:
        nodes_with_successor[previous_node] = [next_node]

    if next_node in nodes_with_predecessors:
        nodes_with_predecessors[next_node].append(previous_node)
    else:
        nodes_with_predecessors[next_node] = [previous_node]


nodes_to_visit = list(set(nodes_with_successor).difference(set(nodes_with_predecessors)))

while nodes_to_visit.__len__() > 0:
    for node in sorted(nodes_to_visit):
        node_predecessors = nodes_with_predecessors.get(node)
        if node_predecessors is None or all(elem in visited_nodes for elem in node_predecessors) and node not in visited_nodes:
            print(node, end="")
            node_successors = nodes_with_successor.get(node)
            if node_successors is None:
                exit()
            nodes_to_visit.extend(node_successors)
            nodes_to_visit.remove(node)

            visited_nodes.add(node)
            break
