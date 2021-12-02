if __name__ == '__main__':
    file = open("day-6-data", "r")
    data = []
    [data.append(line) for line in file.readlines()]

    forms = []
    questions = set()
    for line in data:
        if line is "\n":
            forms.append(questions)
            questions = set()
        else:
            questions.update(line[:-1])

    forms.append(questions)

    print("First part answer: " + str(sum([len(x) for x in forms])))

    forms = []
    for line in data:
        if line is "\n":
            forms.append(questions)
            questions = None
        elif questions is None:
            questions = line[:-1]
        else:
            questions = [x for x in questions if x in line[:-1]]

    forms.append(questions)

    print("Second part answer: " + str(sum([len(x) for x in forms])))
