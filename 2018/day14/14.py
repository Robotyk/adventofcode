def part_a_solution(size):
    recipes = ["3", "7"]
    i = 0
    j = 1

    while len(recipes) < size + 10:
        first_current_recipe = int(recipes[i])
        second_current_recipe = int(recipes[j])

        sum = first_current_recipe + second_current_recipe
        if sum < 10:
            recipes.append(str(sum)[0])
        else:
            recipes.append(str(sum)[0])
            recipes.append(str(sum)[1])

        i = (first_current_recipe + 1 + i) % len(recipes)
        j = (second_current_recipe + 1 + j) % len(recipes)

    return [recipes[a] for a in range(size, size + 10)]


def part_b_solution(input):
    sequence = [i for i in input]

    recipes = ["3", "7"]
    i = 0
    j = 1

    while True:
        first_current_recipe = int(recipes[i])
        second_current_recipe = int(recipes[j])

        sum = first_current_recipe + second_current_recipe
        if sum < 10:
            recipes.append(str(sum)[0])
        else:
            recipes.append(str(sum)[0])
            recipes.append(str(sum)[1])

        i = (first_current_recipe + 1 + i) % len(recipes)
        j = (second_current_recipe + 1 + j) % len(recipes)

        k = len(recipes) - len(sequence) - 1
        if k >= 0 and matches(k, recipes, sequence):
            return k


def matches(k, recipes, sequence):
    l = k
    for i in sequence:
        if recipes[l] != i:
            return False
        l += 1
    return True


print(part_a_solution(825401))
print(part_b_solution("825401"))
