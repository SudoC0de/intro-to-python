# Given a number, print its factorial.
factorial = 5
result = 1

for number in range(1,factorial + 1):
    result *= number

print(f"Factorial {factorial}: {result}")
