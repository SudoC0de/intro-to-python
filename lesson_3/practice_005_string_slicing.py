# Given the string "Python programming is fun!"

# 1. Slice the string and print the substring "programming".
# 2. Slice the string and print the substring "programming is fun!"
# 3. Slice the string and print the substring “Ph rgamn sfn”
string = "Python programming is fun!"
print(string[7:18])
print(string[7:])
print(f'{string[0:6:3]} {string[8:18:2]} {string[20:26:2]}')