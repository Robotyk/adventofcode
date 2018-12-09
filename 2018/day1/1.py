current_sum = 0
set_of_sums = set()
while 1:
    file_object = open("data", "r")
    for x in file_object:
        if x.startswith("-"):
            current_sum -= int(x[1:])
        else:
            current_sum += int(x[1:])
        if current_sum in set_of_sums:
            print(current_sum)
            exit(0)
        set_of_sums.add(current_sum)
