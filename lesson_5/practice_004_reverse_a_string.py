# The [::-1] slicing syntax starts from the end of the string
# (index -1) and goes backward with a step of -1, effectively
# reversing the string.

reversed_string = input("Enter a string: ")
print(reversed_string[::-1])