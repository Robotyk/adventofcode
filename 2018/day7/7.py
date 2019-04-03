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


def get_tasks_order():
    order = ""
    while nodes_to_visit.__len__() > 0:
        for node in sorted(nodes_to_visit):
            node_predecessors = nodes_with_predecessors.get(node)
            if node_predecessors is None or all(
                    elem in visited_nodes for elem in node_predecessors) and node not in visited_nodes:
                order = order + node
                node_successors = nodes_with_successor.get(node)
                if node_successors is None:
                    return order
                nodes_to_visit.extend(node_successors)
                nodes_to_visit.remove(node)

                visited_nodes.add(node)
                break


ordered_tasks = get_tasks_order()
print(ordered_tasks)


# PART B SOLUTION #

tasks_to_do = set(ordered_tasks)
time = 0
completed_tasks = set()
workers_id_to_task_map = {}
workers_id_to_time_left_map = {}


def assign_task(worker_id):
    if worker_id not in workers_id_to_task_map and tasks_to_do:
        for task in tasks_to_do:
            if task not in nodes_with_predecessors or set(nodes_with_predecessors[task]) <= completed_tasks:
                workers_id_to_task_map[worker_id] = task
                workers_id_to_time_left_map[worker_id] = ord(task) - 4
                tasks_to_do.remove(task)
                return


def update_time_left(worker_id):
    if worker_id in workers_id_to_task_map:
        workers_id_to_time_left_map[worker_id] = workers_id_to_time_left_map[worker_id] - 1


def check_if_task_has_ended(worker_id):
    if worker_id in workers_id_to_task_map and workers_id_to_time_left_map[worker_id] == 0:
        workers_id_to_time_left_map.pop(worker_id)
        completed_tasks.add(workers_id_to_task_map.pop(worker_id))


number_of_workers = 5

while workers_id_to_task_map or tasks_to_do:

    for i in range(0, number_of_workers):
        assign_task(i)

    for i in range(0, number_of_workers):
        update_time_left(i)

    for i in range(0, number_of_workers):
        check_if_task_has_ended(i)

    time = time + 1

    print("DEBUG: time - " + '{:03}'.format(time)
          + " worker 1 - " + workers_id_to_task_map.get(0, " ")
          + " worker 2 - " + workers_id_to_task_map.get(1, " ")
          + " worker 3 - " + workers_id_to_task_map.get(2, " ")
          + " worker 4 - " + workers_id_to_task_map.get(3, " ")
          + " worker 5 - " + workers_id_to_task_map.get(4, " "))

print("Total time: " + str(time))
