# HOMEWORK: Functions
# Read carefully until the end before you start solving the exercises.

# Basic Function
# Define a basic function that only prints Hello. Create the definition using def and the call that executes it.
def display_hello():
    print("Hello")

display_hello()
# ----------------------------------------------------------------------------------------------------------------------

# Basic Function with Parameters
# Define a basic function that prints a greeting taking a given name.
def display_greeting(name):
    print(f"Hello {name}")

display_greeting("Colin")
# ----------------------------------------------------------------------------------------------------------------------

# Basic Function with Default Values
# Define a basic function that prints a greeting for a name, but if none is given, use stranger instead of the name,
# so it behaves like this:

# Prints: Hello, stranger!
# greeting()

# Prints: Hello, Tom!
# greeting('Tom')
def dispplay_greeting_defaults(name="stranger"):
    print(f"(Defaults) Hello, {name}")

dispplay_greeting_defaults()
dispplay_greeting_defaults("Colin")

# ----------------------------------------------------------------------------------------------------------------------

# Multiple Parameters
# Define a function that takes two parameters, add them up and prints the sum.

# Prints: The sum of 1 + 2 = 3
# add(1, 2)

# Prints (default values might be useful): The sum of 1 + 0 = 1
# add(1)
def sum(x=0,y=0):
    print(f"Sum: {x + y}")

sum(1,2)
sum(1)

# ----------------------------------------------------------------------------------------------------------------------

# Parameters out of order
# Define a function that takes a first_name and a last_name and prints a full_name. Define the function and create
# the function call in such a way that first_name and last_name can be given in any order and the printed full_name
# would still be correct.

# Prints: Nelson Mandela
# full_name("Nelson", "Mandela")

# Is there anything you can add to the line below, so the function also prints "Nelson Mandela"?
# full_name("Mandela", "Nelson")
def display_full_name(first,last):
    print(f"Full Name: {first} {last}")

display_full_name(last="Mandela",first="Nelson")

# ----------------------------------------------------------------------------------------------------------------------

# Returning Values
# Define a validator function that you can use to determine if a word is longer than 8 characters.
# After creating the function, make sure to test it. Create a list of words and iterate over this
# list using a for loop.

# Tip: Validator functions return True / False which we can use in conditionals to do things like print a message.
word_list = ["word","two","returnfalsehere"]
def word_length_check(word):
    return len(word) > 8

for word in word_list:
    print(f"Is the length of \"{word}\" longer than 8 characters? {word_length_check(word)}")

# ----------------------------------------------------------------------------------------------------------------------

# You're going to revisit some of the algorithms you've already solved. But this time, there's a twist! Your challenge
# is to solve and encapsulate each algorithm into its own Python function. This will not only help you review these
# algorithms but also give you valuable practice in defining and using functions.

# FizzBuzz
# You remember FizzBuzz, right?
# You print Fizz for multiples of 3, Buzz for multiples of 5, and FizzBuzz for multiples of both 3 and 5.

# Now, your task is to take your existing FizzBuzz code and wrap it into a function called fizzbuzz.

# Requirements:
# - Create a function named fizzbuzz that takes a single argument, number.
# - If the number is a multiple of both 3 and 5, the function should return: FizzBuzz
# - If the number is a multiple of 3, the function should return: Fizz
# - If the number is a multiple of 5, the function should return: Buzz
# - Otherwise, the function should return the number.

# Call the function here
def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")

fizzbuzz(15)
fizzbuzz(9)
fizzbuzz(10)

# ----------------------------------------------------------------------------------------------------------------------

# Anagram
# Your next challenge is to implement a function that checks if two given strings are anagrams of each other.
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase. For example,
# "listen" is an anagram of "silent".

# What You Need to Check
# - The two strings must have the same length.
# - The sorted form of the first string must be equal to the sorted form of the second string.

# Approach
# - Create a function that takes two strings as arguments.
# - Check if the lengths are equal. If they're NOT equal, return False (anagrams are always same length).
# - Sort both strings. If the sorted versions are equal, they're anagrams!

# Test your function with these strings
test_str1 = 'abcde'
test_str2 = 'edcba'

def anagram_check(word1="",word2=""):
    if len(word1) == len(word2):
        if sorted(word1) == sorted(word2):
            return True
        else:
            return False
    else:
        return False

if anagram_check(test_str1,test_str2):
    print(f"{test_str2} is an anagram of {test_str1}")
else:
    print(f"{test_str2} is not an anagram of {test_str1}")

# ----------------------------------------------------------------------------------------------------------------------

# Find Max number
# Create a function to find the largest number in a list without using the built-in max() function.

# - Define a function called find_max that takes a list of numbers as an argument.
# - Initialize a variable result and set it to the 1st item of the list using [0]
#   - This variable will hold the largest number as we iterate through the list.
# - Loop through each number in the list.
# - Check if number > result
#   - If it is, update result with the new greater number.
# - return result

# Define your function here

# Test the function with a sample list of numbers.

# Output should be the maximum number in the list.
def find_max(numbers=[0]):
    result = numbers[0]

    for number in numbers:
        if number > result:
            result = number

    return result

number_list = [1,3,2,8,9,6]
print(f"Number List: {number_list}")
print(f"Max number: {find_max(number_list)}")

# ----------------------------------------------------------------------------------------------------------------------

# Even/Odd Checker Function
# Your task is to write a function that determines if a given integer is even or odd. The function should
# print Even for even numbers and Odd for odd numbers.

# What You Need to Check
# - Determine whether the input number is even or odd.
# - An even number can be exactly divided by 2 without a remainder.
# - An odd number leaves a remainder of 1 when divided by 2.

# Define a function is_even_odd(number) here

# Test the function calling it using a variety of numbers like: 1, 10, 5.5, 9
def is_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

list_of_numbers = [1,10,5.5,9]
print(f"List of numbers: {list_of_numbers}")

for number in list_of_numbers:
    print(f"Number \"{number}\" is {is_even_odd(number)}")
