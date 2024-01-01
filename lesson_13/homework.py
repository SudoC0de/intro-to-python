# Homework Lesson 13 - Workshop - Homework

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

################################################################################
### When solving coding challenges, think about the time complexity (Big O). ###
################################################################################

# Challenge 1
# Common Elements Finder

# Given two lists of integers, find and return a new list containing elements that appear in both lists.
# Make sure the resulting list does not contain duplicates.

# Example:

# Input:
# List 1: [1, 2, 3, 4, 5]
# List 2: [4, 5, 6, 7, 8]
# Output: [4, 5]

# Hints:
# You'll need to use nested loops: The outer loop will iterate over elements in the first list,
# and the inner loop will check if that element exists in the second list.
# Keep track of the common elements found so far to ensure no duplicates are added to the resulting list.
# To ensure no duplicates are added to the resulting list,
# check if an element is already present in the "common" list before appending it.

def find_common_elements(list1, list2):
    common = []
    # Your code here
    for number in list1:
        if (number in list2) and (number not in common):
            common.append(number)

    return common

list_1 = [1, 2, 3, 4, 5]
list_2 = [4, 5, 6, 7, 8]
print(find_common_elements(list_1,list_2))

# ---------------------------------------------------------------------

# Refresher
# One of the key skills during job interviews
# is to be able to modify the code you've created.
# The following two tasks are the extension of the recipe problem you solved in class.

# Let's refresh the problem you solved in the class.
# You have a list of recipes, where each recipe contains the ingredients each recipe needs:
# recipes = [
# ["yeast","flour"],
# ["bread","meat"],
# ["flour","meat"]
# ]

# Solution
def find_makeable_recipes(recipes, ingredients):
    makeable_recipes = []
    for recipe in recipes:
        can_make = True
        for ingredient in recipe:
            if ingredient not in ingredients:
                can_make = False
                break
        if can_make:
            makeable_recipes.append(recipe)
    return makeable_recipes


test_recipes = [["yeast", "flour"], ["bread", "meat"], ["flour", "meat"]]
test_ingredients = ["yeast", "flour", "meat"]
test_result = find_makeable_recipes(test_recipes, test_ingredients)
print(test_result)

# ---------------------------------------------------------------------

# Challenge 2
# Missing ingredients

# You have a new list of recipes and ingredients.

# recipes = [
# ["yeast", "flour"],
# ["bread", "meat", "flour"]
# ]

# ingredients = ["yeast","bread"]

# Return the list of missing ingredients for all the recipes.

# Output: ["flour","meat"]


def find_missing_ingredients(recipes, ingredients):
    # Create an empty list to store the missing ingredients
    missing_ingredients = []
    # In the outer loop iterate through each recipe in the list of recipes.
    for recipe in recipes:
        # In the inner loop check each ingredient in the recipe.
        for ingredient in recipe:
            # Check if the ingredient is not in the list of available ingredients
            # and is not already in the list of missing ingredients.
            if (ingredient not in ingredients) and (ingredient not in missing_ingredients):
                # If both conditions are met, add the ingredient to the missing_ingredients list.
                missing_ingredients.append(ingredient)

    # Return the list of missing ingredients required for all the recipes.
    return missing_ingredients

recipes = [
    ["yeast", "flour"],
    ["bread", "meat", "flour"]
]
ingredients = ["yeast","bread"]

print(find_missing_ingredients(recipes,ingredients))

# ---------------------------------------------------------------------

# Challenge 3
# The best recipe

# You have a new list of recipes, where each recipe contains the ingredients it needs.

# recipes = [
# ["yeast","flour"],
# ["bread","meat"],
# ["flour","meat", "yeast"]
# ]

# You also have a list of available ingredients.
# ingredients = ["yeast","flour", "meat", "salt"]

# Return the list of the best recipe (the one that uses most of ingredients).

# Output: ["flour","meat", "yeast"]


def find_best_recipe(recipes, ingredients):
    # Initialize variables to remember the best recipe and the most ingredients used.
    best_recipe = None
    max_used_ingredients = 0

    # Create an outer for loop to go through each recipe in the list of recipes.
    for recipe in recipes:
        # Create an empty list (used_ingredients) to store the ingredients we can use from this recipe.
        used_ingredients = []

        # Create an inner foor loop to look at each ingredient in this recipe.
        for ingredient in recipe:
            # Check if the ingredient is in our list of available ingredients.
            if ingredient in ingredients:
                # If it's available, add it to our list of used ingredients.
                used_ingredients.append(ingredient)

        # Check if the current recipe uses more ingredients (using `len` to count)
        # than the highest count we've recorded so far (max_used_ingredients).
        if len(used_ingredients) > max_used_ingredients:
            # If the current recipe has a higher ingredient count, update max_used_ingredients.
            max_used_ingredients = len(used_ingredients)
            # Then set this recipe as the new best.
            best_recipe = recipe

    # Finally, return the best recipe that uses the most ingredients.
    return best_recipe

# Define the list of recipes and available ingredients.
recipes = [
    ["yeast","flour"],
    ["bread","meat"],
    ["flour","meat", "yeast"]
]
ingredients = ["yeast","flour", "meat", "salt"]
# Call the function to find the best recipe and print the result.
print(find_best_recipe(recipes,ingredients))

# ---------------------------------------------------------------------

# Challenge 4
# Find a peak element
# You are given an array of integers, and your goal is to find a "peak" element in the array.
# A peak element is an element that is strictly greater than its adjacent elements (elements on the left and on the right).

# Write a Python function find_peak_element(arr) that takes an array of integers as input
# and returns the index of the peak element in the array.

# Handle edge cases:
# - If the array has fewer than three elements, return -1.

# Check each element in the array:

# - If an element is strictly greater than both its adjacent elements (if they exist), consider it a peak element.
# - Return the index of the first peak element you find.
# - If no peak elements are found, return -1.

# Example:
# arr1 = [1, 3, 20, 4, 1, 0]
# result1 = find_peak_element(arr1)
# print(result1)  # Output: 2 (Peak element: 20)

# arr2 = [1, 2, 3, 4, 5]
# result2 = find_peak_element(arr2)
# print(result2)  # Output: -1 (No peak elements)

# arr3 = [5, 10, 20, 15]
# result3 = find_peak_element(arr3)
# print(result3)  # Output: 2 (Peak element: 20)


def find_peak_element(arr):
    n = len(arr) # Find out how many elements are in the array

    # Check for the edge case (less than 3 elements)
    if n < 3:
        return -1

    # Check the first and last element separately as they don't have neighbors
    # Iterate over the range, excluding the first and last indices, as they lack one neighbor.
    peak_index = -1

    for index in range(1, (len(arr) - 1)):
        is_peak = True

        for nested_index in range(index - 1, -1, -1):
            if arr[nested_index] > arr[index]:
                is_peak = False
                break

        if is_peak == True:
            for nested_index in range(index + 1, len(arr)):
                if arr[nested_index] > arr[index]:
                    is_peak = False
                    break

            if is_peak == True:
                peak_index = index
                break

    # Return -1 # if no peak element is found.
    if peak_index == -1:
        return -1

    return peak_index

arr1 = [1, 3, 20, 4, 1, 0]
arr2 = [1, 2, 3, 4, 5]
arr3 = [5, 10, 20, 15]
print(find_peak_element(arr1))
print(find_peak_element(arr2))
print(find_peak_element(arr3))

# ---------------------------------------------------------------------

# Challenge 5 (optional)
# Delete duplicates in sorted lists

# Given a sorted list of integers, write a program that:

# - Removes all duplicate values from the list.
# - Shifts the unique values to the left to fill any emptied indices.
# - Fills the remaining rightmost indices with zeroes.
# - Returns the count of unique values in the list.

# - Example:
# Input: [1, 2, 2, 3, 4, 4, 4, 5]
# Output: [1, 2, 3, 4, 5, 0, 0, 0], 5 (5 unique values)

# Hints:
# - Sequential Comparison: Since the list is sorted, duplicates will always be adjacent to each other.
# Compare each element to the previous one to detect duplicates.
# - Updating in Place: You can modify the original list as you find unique numbers
# and move them to the correct position. Think of this position as where the next unique number should go.

def delete_duplicates(arr):
    # 'write_index' points to where the next unique element should be written.
    write_index = 1

    # Iterate over the list's length, starting from the second element because
    # the first element doesn't have a previous element to compare against.
    for index in range(1,len(arr)):
        # Compare the current element with its immediate previous element.
        if arr[index] != arr[index - 1]:
            # If they're different, it's not a duplicate.
            # Place the current element at the 'write_index' position.
            arr[write_index] = arr[index]
            # Then increment 'write_index' by 1 to prepare for the next unique element.
            write_index += 1

    # Once you have shifted all unique elements to the left,
    # fill the remaining positions in the list with zeroes.
    for i in range(write_index, len(arr)):
        arr[i] = 0

    # Return the modified list for visualization and the count of unique elements.
    return arr

input_list = [1, 2, 2, 3, 4, 4, 4, 5]
print(delete_duplicates(input_list))
