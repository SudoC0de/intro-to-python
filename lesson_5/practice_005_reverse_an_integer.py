# Given an integer, return the integer with reversed digits.
#
# Note:
# The integer could be either positive or negative.
#
# Example:
# -876 -> -678

number = int(input("Enter a number: "))

if number >= 0:
    print(str(number)[::-1])
else:
    print(f"-{str(number)[:0:-1]}")