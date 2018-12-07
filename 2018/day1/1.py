currentSum = 0
setOfSums = {0}
while 1:
    file_object = open("data", "r")
    for x in file_object:
        if x.startswith("-"):
            currentSum -= int(x[1:])
        else:
            currentSum += int(x[1:])
        if currentSum in setOfSums:
            print(currentSum)
            exit(0)
        setOfSums.add(currentSum)
