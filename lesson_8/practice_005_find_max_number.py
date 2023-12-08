# Your goal is to write a Python program that finds the maximum number in a given list of numbers.
# Example:
# numbers = [1, 2, 42, 77, 99, -100]
# Output: 99
numbers = [1, 2, 42, 77, 99, -100]
result = 0

for number in numbers:
    if number > result:
        result = number

print(result)
print(sorted(numbers)[-1])
