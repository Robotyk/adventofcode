def validate_passwords():
    first_counter, second_counter = 0, 0
    for line in file.readlines():
        hyphen_index = line.find("-")
        colon_index = line.find(":")

        first_number = int(line[:hyphen_index])
        second_number = int(line[hyphen_index + 1:colon_index - 2])
        letter = line[colon_index - 1:colon_index]
        password = line[colon_index + 2:]

        number_of_occurrence = password.count(letter)
        if first_number <= number_of_occurrence <= second_number:
            first_counter += 1

        if (password[first_number - 1] == letter) != (password[second_number - 1] == letter):
            second_counter += 1

    return first_counter, second_counter


if __name__ == '__main__':
    file = open("day-2-data", "r")

    validated_passwords = validate_passwords()
    print("First part answer: " + str(validated_passwords[0]))
    print("Second part answer: " + str(validated_passwords[1]))

    file.close()
