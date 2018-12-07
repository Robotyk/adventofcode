file_object = open("data", "r")
packageIds = []
for packageId in file_object:
    packageId = packageId[:-1]
    encodedPackageId = ""
    for y in list(packageId):
        encodedLetter = (ord(y) + 3) % 100
        if encodedLetter < 10:
            encodedPackageId += "0" + str(encodedLetter)
        else:
            encodedPackageId += str(encodedLetter)
    packageIds.append((encodedPackageId, packageId))

result = ()

for i in range(0, packageIds.__len__() - 1):
    for j in range(i+1, packageIds.__len__()):
        difference = int(packageIds[i][0]) - int(packageIds[j][0])
        counter = 0
        for digit in str(difference):
            if digit != "0":
                counter += 1
        if counter <= 2:
            encodedPackageId = str(abs(difference))[1:]
            if int(encodedPackageId) == 0:
                result = (packageIds[i][1], packageIds[j][1])
for i in range(0, result[0].__len__()):
    if result[0][i] != result[1][i]:
        commonLetters = result[0].replace(result[0][i], "", 1)
        break
print(commonLetters)
