def init_empty_dict():
    empty_dictionary = {}
    for i in range(60):
        empty_dictionary[i] = 0
    return empty_dictionary


def update_dict(dict, current_line, next_line):
    for i in range(int(current_line[15:17]), int(next_line[15:17])):
        dict.update({i: dict.get(i) + 1})
    return dict


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
        if guard_to_minutes_slept.get(current_guard) is None:
            empty_dict = init_empty_dict()
            dict = update_dict(empty_dict, guard_schedule[i], guard_schedule[i + 1])
            guard_to_minutes_slept[current_guard] = dict
            i += 1
        else:
            guard_to_minutes_slept.update({current_guard: update_dict(guard_to_minutes_slept.get(current_guard), guard_schedule[i], guard_schedule[i + 1])})
            i += 1
    else:
        current_guard = current_line[int(current_line.find("#") + 1):int(current_line.find(" ", current_line.find("#") + 1))]
    i += 1

current_highest_minutes_amount = 0
highest_minutes = 0
guard_with_highest_minutes = 0

for guard_id in guard_to_minutes_slept:
    for minute in guard_to_minutes_slept.get(guard_id):
        if guard_to_minutes_slept.get(guard_id).get(minute) > current_highest_minutes_amount:
            current_highest_minutes_amount = guard_to_minutes_slept.get(guard_id).get(minute)
            highest_minutes = int(minute)
            guard_with_highest_minutes = int(guard_id)

print(highest_minutes * guard_with_highest_minutes)