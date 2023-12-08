# Given a list.
# Calculate sum and multiplication of all elements.
# Print the list, sum and multiplication of elements.
# For example:
# Input: [1, 2, 3, 4]
# Output sum: 10
# Output multiplication: 24
import math

numbers = [1, 2, 3, 4]
add_answer = 0
mult_answer = 1

for number in numbers:
    add_answer += number
    mult_answer *= number

print(add_answer)
print(mult_answer)
