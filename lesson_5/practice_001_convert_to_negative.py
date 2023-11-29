# Create a variable called number. Set it to any number.

# Convert the number to negative and print it.
# Keep the number as is, if the number is already negative.

# 5 => -5
# -1 => -1

number = float(input("Enter a number: "))

if number < 0:
    print(number)
elif number > 0:
    print(number * -1)
else:
    print(0)