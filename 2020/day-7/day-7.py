import re


def find_parents(element):
    parents = [x for x in bags if element.name in [y[1].name for y in x.bags_inside]]
    all_parents = set([x.name for x in parents])
    for parent in parents:
        all_parents.update(find_parents(parent))

    return all_parents


def find_children(element):
    for inner_bag_tuple in element.bags_inside:
        inner_bag = inner_bag_tuple[1]

        found_child_bag = [x for x in bags if inner_bag.name in x.name][0]

        inner_bag.bags_inside = found_child_bag.bags_inside

        find_children(inner_bag)
    return element


def count_bags(element):
    counter = 1

    for inner_bag_tuple in element.bags_inside:
        inner_bag_quantity = int(inner_bag_tuple[0])

        counter += inner_bag_quantity * count_bags(inner_bag_tuple[1])
    return counter


class Bag:
    def __init__(self, name, bags_inside):
        self.name = name
        self.bags_inside = bags_inside


if __name__ == '__main__':
    file = open("day-7-data", "r")
    bags = []
    for line in file.readlines():
        split = line.split()
        bag_name = split[0] + " " + split[1]
        bags_inside = []
        for i in range(2, len(split)):
            if re.match("\\d", split[i]):
                bags_inside.append((split[i], Bag(split[i + 1] + " " + split[i + 2], [])))
                i += 3
        bags.append(Bag(bag_name, bags_inside))

    root = [x for x in bags if "shiny gold" in x.name][0]

    print("First part answer: " + str(len(find_parents(root))))

    print("Second part answer: " + str(count_bags(find_children(root)) - 1))