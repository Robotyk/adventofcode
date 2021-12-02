def find_earliest_bus(bus_departures):
    i = departure_timestamp
    while True:
        for x in bus_departures:
            if i % x == 0:
                return x, i - departure_timestamp
        i += 1


def calculate_schedule(bus_departures):
    known_bus_departures = []
    for i in range(len(bus_departures)):
        if bus_departures[i] != "x":
            known_bus_departures.append((int(bus_departures[i]), i))
    max_step = max(known_bus_departures)
    i = max_step[0] - max_step[1]
    while True:
        match = True
        for j in known_bus_departures:
            if ((i + j[1]) % j[0]) != 0:
                match = False
            if not match:
                break
        if match:
            return i
        i += max_step[0]


if __name__ == '__main__':
    with open("day-13-data", "r") as f:
        departure_timestamp = int(f.readline())
        bus_departures = f.readline().split(",")

    earliest_bus = find_earliest_bus([int(x) for x in bus_departures if x != "x"])
    print("First part answer: " + str(earliest_bus[0] * earliest_bus[1]))
    print("Second part answer: " + str(calculate_schedule(bus_departures)))
