with open("data", "r") as file:
    generators = {}
    initial = file.readline()[15:115]
    file.readline()
    for line in file:
        generators[line[:5]] = line[9:10]


pots = ".........." + initial + "...................."


def calculate(pots):
    sum = 0
    for i in range(len(pots)):
        if pots[i] == "#":
            sum += (i - 10)
    return sum


for i in range(20):
    next_generation_plants = ".."
    for j in range(len(pots) - 4):
        neighbours = pots[j:j + 5]
        next_generation_plants += generators[neighbours]

    pots = next_generation_plants + ".."


print(str(calculate(pots)))
