import sys

if __name__ == '__main__':
    file = open("data", "r")
    data = [int(i) for i in file.readlines()]
    file.close()

    previous = sys.maxsize
    counter = 0

    for line in data:
        if line > previous:
            counter += 1
        previous = line

    print("First part solution: " + str(counter))

    previous = sys.maxsize
    counter = 0
    for i in range(1, len(data) - 1):
        current = data[i - 1] + data[i] + data[i + 1]
        if current > previous:
            counter += 1
        previous = current

    print("Second part solution: " + str(counter))
