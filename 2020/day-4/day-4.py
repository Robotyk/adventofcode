import re

def prepare_data():
    file = open("day-4-data", "r")
    data = []
    passport = {}
    for line in file.readlines():
        if line is not "\n":
            line = line[:len(line) - 1]
            for pair in line.split(" "):
                parts = pair.split(":")
                passport[parts[0]] = parts[1]
        else:
            data.append(passport)
            passport = {}
    data.append(passport)
    file.close()

    return data


if __name__ == '__main__':
    data = prepare_data()

    data = [x for x in data if all(key in x.keys() for key in {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"})]
    print("First part answer: " + str(len(data)))

    valid_passports_quantity = 0

    for passport in data:
        if re.match("^(19[2-9]\d|200[0-2])$", passport.get("byr")) \
                and re.match("^(201\d|2020)$", passport.get("iyr")) \
                and re.match("^(202\d|2030)$", passport.get("eyr")) \
                and re.match("^(1[5-8]\dcm|19[0-3]cm|59in|6\din|7[0-6]in)$", passport.get("hgt")) \
                and re.match("^#([\da-f]){6}$", passport.get("hcl")) \
                and re.match("^(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)$", passport.get("ecl")) \
                and re.match("^\d{9}$", passport.get("pid")):

            valid_passports_quantity += 1

    print("Second part answer: " + str(valid_passports_quantity))