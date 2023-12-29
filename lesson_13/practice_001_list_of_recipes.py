# You have a list of recipes, where each recipe contains the ingredients each recipe needs:
recipes = [
    ["yeast", "flour"],
    ["bread", "meat"],
    ["flour", "meat"]
]

# You also have a list of available ingredients.
ingredients = ["yeast", "flour", "meat"]


# Return a list of all recipes that can be made with the ingredients you have.
# Output: [["yeast","flour"], ["flour","meat"]]

def makeable_recipes(recipes, ingredients):
    # Your code here
    complete_recipes = []

    for recipe in recipes:
        makeable = True

        for ingredient in recipe:
            if ingredient not in ingredients:
                makeable = False
                break

        if makeable == True:
            complete_recipes.append(recipe)

    return complete_recipes

print(makeable_recipes(recipes,ingredients))
