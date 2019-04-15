def create_recipe(size):
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


print(create_recipe(825401))