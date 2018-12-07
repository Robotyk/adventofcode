import operator


def calculate_mins(current_line, next_line):
    return int(next_line[15:17]) - int(current_line[15:17])


def update_sleepy_minutes(sleepy_minutes, current_line, next_line):
    for j in range(int(current_line[15:17]), int(next_line[15:17])):
        if sleepy_minutes.get(j) is None:
            sleepy_minutes[j] = 1
        else:
            sleepy_minutes.update({j: (sleepy_minutes.get(j) + 1)})


file_object = open("data", "r")
guardSchedule = []
for i in file_object:
    guardSchedule.append(i)
guardSchedule.sort()

guardToMinutesSlept = {}
i = 0
while i < guardSchedule.__len__():
    currentLine = guardSchedule[i]
    if "#" not in currentLine:
        sleptMins = calculate_mins(currentLine, guardSchedule[i + 1])
        i += 1
        if guardToMinutesSlept.get(currentGuard) is None:
            guardToMinutesSlept[currentGuard] = sleptMins
        else:
            guardToMinutesSlept.update({currentGuard: (guardToMinutesSlept.get(currentGuard) + sleptMins)})
    else:
        currentGuard = currentLine[int(currentLine.find("#") + 1):int(currentLine.find(" ", currentLine.find("#") + 1))]
    i += 1
sleepyHeadGuard = max(guardToMinutesSlept.items(), key=operator.itemgetter(1))[0]

sleepyMinutes = {}
i = 0
while i < guardSchedule.__len__():
    currentLine = guardSchedule[i]
    if "#" + sleepyHeadGuard in currentLine:
        i += 1
        while "#" not in guardSchedule[i]:
            update_sleepy_minutes(sleepyMinutes, guardSchedule[i], guardSchedule[i + 1])
            i += 2
    else:
        i += 1
sleepyMinute = max(sleepyMinutes.items(), key=operator.itemgetter(1))[0]
result = int(sleepyHeadGuard) * sleepyMinute
print(result)
