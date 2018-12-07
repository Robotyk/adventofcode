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
guard_schedule = []
for i in file_object:
    guard_schedule.append(i)
guard_schedule.sort()

guard_to_minutes_slept = {}
i = 0
while i < guard_schedule.__len__():
    current_line = guard_schedule[i]
    if "#" not in current_line:
        slept_mins = calculate_mins(current_line, guard_schedule[i + 1])
        i += 1
        if guard_to_minutes_slept.get(current_guard) is None:
            guard_to_minutes_slept[current_guard] = slept_mins
        else:
            guard_to_minutes_slept.update({current_guard: (guard_to_minutes_slept.get(current_guard) + slept_mins)})
    else:
        current_guard = current_line[int(current_line.find("#") + 1):int(current_line.find(" ", current_line.find("#") + 1))]
    i += 1
sleepy_head_guard = max(guard_to_minutes_slept.items(), key=operator.itemgetter(1))[0]

sleepy_minutes = {}
i = 0
while i < guard_schedule.__len__():
    current_line = guard_schedule[i]
    if "#" + sleepy_head_guard in current_line:
        i += 1
        while "#" not in guard_schedule[i]:
            update_sleepy_minutes(sleepy_minutes, guard_schedule[i], guard_schedule[i + 1])
            i += 2
    else:
        i += 1
sleepy_minute = max(sleepy_minutes.items(), key=operator.itemgetter(1))[0]
result = int(sleepy_head_guard) * sleepy_minute
print(result)
