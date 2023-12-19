# Homework Lesson 10 - Workshop - Homework

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

################################################################################
### When solving coding challenges, think about the time complexity (Big O). ###
################################################################################

# Challenge 1
# Multiplication of a three-digit number
#
# A program gets a three-digit number and has to multiply all its digits.
# For example, if a number is 349, the code has to print the number 108, because 3*4*9 = 108.
#
# Hints:
# Use the modulus operator % to get the last digit.
# Use floor division to remove the last digit

def multiplication_of_three(number):
# Your code here
    result = 1

    for integer in range(0, 3):
        result *= (number % 10)
        number //= 10

    return result

print(multiplication_of_three(349))

# ---------------------------------------------------------------------

# Challenge 2
# Sum and multiplication of even and odd numbers.
#
# You are given an array of integers. Your task is to calculate two values: the sum of
# all even numbers and the product of all odd numbers in the array. Please return these
# two values as a list [sum_even, multiplication_odd].
#
# Example
# For the array [1, 2, 3, 4]:
#
# The sum of all even numbers is 2 + 4 = 6.
# The product of all odd numbers is 1 * 3 = 3.
# The function should return the list [6, 3].

def sum_even_and_product_odd(arr):
    # Initialize variables for the sum of even numbers and the product of odd numbers
    sum_even = 0
    product_odd = 1
    # Your code here
    for number in arr:
        if number % 2 == 0:
            sum_even += number
        else:
            product_odd *= number

    return [sum_even,product_odd]

argument = [1, 2, 3, 4]
print(sum_even_and_product_odd(argument))

# ---------------------------------------------------------------------

# Challenge 3
# Invert a list of numbers
#
# Given a list of numbers, return the inverse of each. Each positive becomes a negative,
# and the negatives become positives.
#
# Example:
# Input: [1, 5, -2, 4]
# Output: [-1, -5, 2, -4]

def invert_list(arr):
# Your code here
    for index in range(len(arr)):
        if arr[index] < 0 or arr[index] > 0:
            arr[index] *= -1

    return arr

argument = [1, 5, -2, 4]
print(invert_list(argument))

# ---------------------------------------------------------------------

# Challenge 4
# Difference between
#
# Implement a function that returns the difference between the largest and the
# smallest value in a given list.
# The list contains positive and negative numbers. All elements are unique.
#
# Example:
# Input: [3, 5, 7, 2]
# Output: 7 - 2 = 5

def max_diff(arr):
    # Check if the list is empty
    # If it is, return 0 as there's no difference to be calculated
    if len(arr) == 0:
        return 0


# If the list is not empty,
# proceed with the rest of the code.

# Your code here
    min = arr[0]
    max = arr[0]

    for number in arr:
        if number < min:
            min = number
        elif number > max:
            max = number

    return max - min

argument = [3, 5, 7, 2]
print(max_diff(argument))

# ---------------------------------------------------------------------

# Challenge 5
# Sum between range values
# You are given an array of integers and two integer values, min and max.
# Your task is to write a function that finds the sum of all elements in the
# array that fall within the range [min, max], inclusive.
#
# Example:
# arr = [3, 2, 1, 4, 10, 8, 7, 6, 9, 5]
# min_val = 3
# max_val = 7
#
# Output: 25 (3 + 4 + 5 + 6 + 7)
#
# Hint:  Iterate through each number (num) in the array (arr) and check if the current number  falls within the range [min_val, max_val].

def sum_between_range(arr, min_val, max_val):
# Your code here
    result = 0

    for number in arr:
        if min_val <= number <= max_val:
            result += number

    return result

argument = [3, 2, 1, 4, 10, 8, 7, 6, 9, 5]
min_val = 3
max_val = 7
print(sum_between_range(argument, min_val, max_val))
