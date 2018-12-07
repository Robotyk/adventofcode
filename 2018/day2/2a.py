file_object = open("data", "r")
twoLetters = 0
threeLetters = 0
for x in file_object:
    dictionary = {}
    for y in list(x):
        if dictionary.get(y) is None:
            dictionary[y] = 1
        else:
            dictionary.update({y: (dictionary.get(y) + 1)})
    if 2 in dictionary.values():
        twoLetters += 1
    if 3 in dictionary.values():
        threeLetters += 1
checksum = twoLetters * threeLetters
print(checksum)
