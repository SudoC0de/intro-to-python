# Homework Lesson 5 - Workshop - Homework

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

# Challenge 1
# Make a number Positive
#
# Create a variable called my_number and set it to any integer value.
# Write code to make the number positive if it's negative, and keep it
# as is if it's already positive or zero.
#
# Example:
# Input: -3 => Output: 3
# Input: 5 => Output: 5
my_number = int(input("Enter a number: "))

if my_number < 0:
    my_number *= -1

print(my_number)

# ---------------------------------------------------------------------

# Challenge 2
# BinGo!
#
# If the number is divisible of 3, print “Bin”
# If the number is divisible of 7, print “Go”
# For numbers which are divisible of 3 and 7, print “BinGo”
# Otherwise, print the original number: “{number} is just a number”
another_number = int(input("Enter a number: "))

if (another_number % 3 == 0) and (another_number % 7 == 0):
    print("BinGo")
elif another_number % 3 == 0:
    print("Bin")
elif another_number % 7 == 0:
    print("Go")
else:
    print(f"{another_number} is just a number")

# ---------------------------------------------------------------------

# Challenge 3
# Find the middle number
#
# Given three different numbers x, y, and z, find the number that is neither
# the smallest nor the largest and print it.
#
# Example:
# x = 1, y = 5, z = 3 => Output: 3
x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))
z = int(input("Enter number 3: "))

if x < y < z or x > y > z:
    print(f"Middle number: {y}")
elif y < z < x or y > z > x:
    print(f"Middle number: {z}")
elif z < x < y or z > x > y:
    print(f"Middle number: {x}")

# ---------------------------------------------------------------------

# Challenge 4
# Palindrome Numbers
#
# Ask a user to input a number.
# Write a program to check if the given number is a palindrome.
# It should print True if the number is a palindrome and False if it is not.
#
# Palindrome number: 121, 898
palindrome_number = int(input("Enter a number: "))

if str(palindrome_number) == str(palindrome_number)[::-1]:
    print("Palindrome: True")
else:
    print("Palindrome: False")

# ---------------------------------------------------------------------

# Challenge 5
# Reverse a string
#
# You're part of a team working on analyzing customer reviews for a new video game.
# Due to a software glitch, some reviews have been recorded in reverse with punctuation
# at the beginning instead of the end. Your task is to correct these reviews so that they
# are in the correct order and the punctuation is appropriately placed at the end of the
# sentence or word.
#
# Example: "tcefreP!" -> Perfect!
review_comment = "tcefreP!"
print(review_comment[-2::-1])

#Used the example value to answer but here's the string fully reversed with the puncutation at the beginning as suggested by the challenge description
review_comment = "!tcefreP"
print(review_comment[::-1])
