# Find the max number from 3 values.
#
# Example: 124, 21, 32. Result = 124.

max_number = 0
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if number1 > number2 and number1 > number3:
    max_number = number1
elif number2 > number1 and number2 > number3:
    max_number = number2
elif number3 > number2 and number3 > number1:
    max_number = number3

print(max_number)