file = open("data", "r")
polymer = file.read()


def reduce_polymer(polymer):
    has_sth_changed = True
    while has_sth_changed:
        has_sth_changed = False
        i = 0
        while i < polymer.__len__() - 1:
            if i < 0:
                i = 0
            if i >= polymer.__len__():
                break
            if abs(ord(polymer[i]) - ord(polymer[i + 1])) == 32:
                has_sth_changed = True
                polymer = polymer[:i] + polymer[i + 2:]
                i -= 1
            else:
                i += 1
    return polymer


shortest_polymer_length = 99999
for i in range(97, 123):
    new_polymer = polymer.replace(chr(i), "").replace(chr(i - 32), "")
    polymer_length = reduce_polymer(new_polymer).__len__()
    if polymer_length < shortest_polymer_length:
        shortest_polymer_length = polymer_length

print(shortest_polymer_length)
