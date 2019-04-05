with open("data", "r") as file:
    data = file.readline().split()

number_of_players = int(data[0])
last_marble_worth = int(data[6]) * 100


class Node:
    def __init__(self, name):
        self.value = name


class LinkedList:
    def add(self, node):
        temp = self.current.next.next
        self.current.next.next = node
        node.previous = self.current.next
        node.next = temp
        temp.previous = node
        self.current = node

    def remove(self):
        for i in range(7):
            self.current = self.current.previous
        value = self.current.value
        self.current.previous.next = self.current.next
        self.current = self.current.next
        return value

    def print(self):
        current = self.current.next
        print(str(self.current.value) + " ", end="")
        while current != self.current:
            print(str(current.value) + " ", end="")
            current = current.next


circle = LinkedList()

start_node = Node(0)
start_node.next = start_node
start_node.previous = start_node

score_board = {}
for i in range(number_of_players):
    score_board[i] = 0

circle.current = start_node
for i in range(1, last_marble_worth + 1):
    if i % 23 == 0:
        current_player = i % number_of_players
        score_board[current_player] = score_board[current_player] + circle.remove() + i
    else:
        circle.add(Node(i))

print(max(score_board.values()))