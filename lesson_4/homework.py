# Homework Lesson 4 - Conditionals

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

# ---------------------------------------------------------------------
# Exercise 1: Temperature Classification
# You're developing a weather application. Write a program that takes 
# a temperature in Fahrenheit as input. If the temperature is above 
# 85°F, print "Hot day ahead!".

# <Your code here>
temperature = int(input("Enter the temperature in Fahrenheit: "))

if temperature > 85:
    print("Hot day ahead!")

# ---------------------------------------------------------------------
# Exercise 2: Grade Classifier
# As a teacher, you want to automate grading. Write a program that
# takes a student's score as input and prints "Pass" if the score is
# 50 or above, otherwise print "Fail".
# Do not forget that the input() function returns a string value and
# you need to convert it so you can use the value as a number.

# <Your code here>
score = int(input("Enter student score: "))

if score >= 50:
    print("Pass")
else:
    print("Fail")

# ---------------------------------------------------------------------
# Exercise 3: Scholarship Eligibility
# Your university offers scholarships based on academic performance.
# Write a program that takes a student's GPA as input. If the GPA
# is greater than or equal to 3.5, print
# "Congratulations, you're eligible for a scholarship!". If it's
# between 3.0 and 3.49, print "You're on the waiting list."
# Otherwise, print "Keep up the good work."
# Do not forget that the input() function returns a string value and
# you need to convert it so you can use the value as a number.
# The function int() converts the number to an integer, and the function
# float() converts the number to a float.

# <Your code here>
gpa = float(input("Enter your GPA: "))

if gpa >= 3.5:
    print("Congratulations, you're eligible for a scholarship!")
elif 3.0 <= gpa <= 3.49:
    print("You're on the waiting list.")
else:
    print("Keep up the good work.")

# ---------------------------------------------------------------------
# Exercise 4: Shopping Discount
# A store is offering a discount on a product. Write a program that
# takes the original price and the discount percentage as input.
# If the discounted price is less than $50, print "Great deal!".
# Otherwise, print "Might want to wait for a better offer."

# <Your code here>
original_price = float(input("Enter product original price: "))
discount_percentage = float(input("Enter discount percentage: "))
discounted_price = original_price - (original_price * (discount_percentage / 100))

if discounted_price < 50:
    print("Gread deal!")
else:
    print("Might want to wait for a better offer.")

# ---------------------------------------------------------------------
# Exercise 5: Movie Night Decision
# You and your friends are deciding on a movie to watch. Write a
# program that takes two movie ratings as input. If both ratings
# are above 7, print "Let's watch both!". Otherwise,
# print "Let's just pick one."

# <Your code here>
movie_rating_1 = int(input("Enter movie 1 rating: "))
movie_rating_2 = int(input("Enter movie 2 rating: "))

if movie_rating_1 > 7 and movie_rating_2 > 7:
    print("Let's watch both!")
else:
    print("Let's just pick one.")

# ---------------------------------------------------------------------
# Exercise 6: Restaurant Recommendation
# You're building a restaurant recommendation system. Write a program
# that takes a person's mood (happy or sad) and hunger level
# (high or low) as input. If they're happy and hungry, recommend
# a fancy restaurant. If they're sad and hungry, recommend comfort food.
# For other cases, recommend a casual dining place.

# <Your code here>
mood = input("Enter your mood: ")
hunger_level = input("Enter your hunger level: ")

if mood == "happy" and hunger_level == "high":
    print("I recommend going to a fancy restaurant.")
elif mood == "sad" and hunger_level == "high":
    print("I recommend getting some comfort food")
else:
    print("I recommend going to some casual dining place.")

# ---------------------------------------------------------------------
# Exercise 7: Exercise 7: Tax Bracket Calculator
# You're building a tax calculation system. Write a program that
# takes a person's annual income as input. Use conditionals
# to determine their tax bracket based on the following rules:

# - If income is less than $40,000, tax rate is 10%.
# - If income is between $40,000 and $100,000 (inclusive), tax rate is 20%.
# - If income is greater than $100,000, tax rate is 30%.

# Remember that a tax rate of 10% can be represented as 10/100 or 0.1

# Print the calculated tax amount for the given income.

# <Your code here>
annual_income = float(input("Enter your annual income: "))
tax_rate = 0

if annual_income > 100000:
    tax_rate = 30
elif 40000 <= annual_income <= 100000:
    tax_rate = 20
elif annual_income < 40000:
    tax_rate = 10

tax_amount = annual_income * (tax_rate / 100)

# Print tax amount
print(f"Your tax amount is ${tax_amount}")

# ---------------------------------------------------------------------
# Exercise 8: Ticket Pricing System
# You're working on a ticket booking system for an amusement park.
# Write a program that takes a person's age as input and determines
# their ticket price based on the following rules:
# - Children (ages 3 to 12): $10
# - Adults (ages 13 to 64): $20
# - Seniors (ages 65 and above): $15
# Print the calculated ticket price for the given age.

# <Your code here>
age = int(input("Enter your age: "))
price = 0

if age >= 65:
    price = 15
elif 13 <= age <= 64:
    price = 20
elif 3 <= age <= 12:
    price = 10

print(f"Ticket Price: {price}")

# ---------------------------------------------------------------------
# Exercise 9: Password Strength Checker
# Create a program that takes a password as input and checks its
# strength based on the following rules:

# If the password is less than 8 characters, print "Weak password."
# If the password is 8 to 12 characters long, print "Moderate password."
# If the password is more than 12 characters, print "Strong password

# You can use len() function to get the length of a given string.

# <Your code here>
password = input("Enter your password: ")

if len(password) < 8:
    print("Weak password.")
elif 8 <= len(password) <= 12:
    print("Moderate password")
elif len(password) > 12:
    print("Strong password.")

# ---------------------------------------------------------------------
# CHALLENGE (OPTIONAL): Course Enrollment Eligibility
# To solve this exercise, you will need to use the following concepts
# and methods:
# - String method .upper()
# - String slicing
# - if-elif-else conditional statements
#
# You're designing a course enrollment system. Write a program that
# takes a course code and a student's grade as input and determines
# whether the student is eligible to enroll in the course.

# 1. Ask the user to enter a course code (e.g., "CS101", "MATH202", ).
#    All courses ends with "101", "202" or "303". Slice the string
#    to get the last three character of the string to get the course
#    ending:
#
#    Hint:
#    test = "ABCDEF"  # Given this string
#    print(test[-2:])  # It will print "EF"

# 2. Ask the user to enter their grade (e.g., "A", "B", "C", "D", "F").
#    Use .upper() method to convert the course code and grade to uppercase,
#    allowing for case-insensitive input.
#
# Implement the following enrollment rules:
# - For courses with course codes ending in "101", students with
#   grades "A" or "B" are eligible.
# - For courses with course codes ending in "202", students with
#   grades "B" or "C" are eligible.
# - For courses with course codes ending in "303", students with
#   grades "C" or "D" are eligible.

# Print either "You are eligible to enroll." or "You are not eligible to enroll."

# Convert input to uppercase for case-insensitive comparison

# Extract the last three characters of the course code (use string slicing)

# Check course code and grade to determine eligibility

# <Your code here>
course_code = input("Enter the course code: ")
student_grade = input("Enter your grade: ")
course_code = course_code.upper()
student_grade = student_grade.upper()
course_suffix =  course_code[-3:]

if course_suffix == "101":
    if student_grade in ["A","B"]:
        print("You are eligible to enroll.")
    else:
        print("You are not eligible to enroll.")
elif course_suffix == "202":
    if student_grade in ["A","B","C"]:
        print("You are eligible to enroll.")
    else:
        print("You are not eligible to enroll.")
elif course_suffix == "303":
    if student_grade in ["A","B","C","D"]:
        print("You are eligible to enroll.")
    else:
        print("You are not eligible to enroll.")