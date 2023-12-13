# Create a program that does the following:
#
# 1. Keeps asking for names, one at a time. Stop asking for names when user's input is "end".
# 2. When the user is done adding names, the program should show two lines for each name:
#    - A line with a greeting: "Hello, {name}!"
#    - A line with the first letter of the user's name: "Your initial is {initial}."
#
# Use at least one function. Extra points if you use two and call a function from another function.

def input_full_name():
    first_name = input("Enter first name (Enter \"end\" to quit): ")
    last_name = input("Enter last name (Press Enter to quit): ")

    return f"{first_name} {last_name}"

def create_greeting_one(name):
    return f"Hello, {name}"

def create_greeting_two(name):
    return f"Your initial is {name[0]}"

def present_names(names):
    for name in names:
        print(create_greeting_one(name))
        print(create_greeting_two(name))

names = []
full_name = ""

while full_name != "end":
    full_name = input_full_name()
    full_name = full_name.strip()

    if full_name != "end":
        names.append(full_name)

present_names(names)
