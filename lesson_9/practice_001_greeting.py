# The following program takes a user's name and greets them back.
# Modify the code to use a function to print the greeting instead.

def PrintGreeting():
    user_name = input("What's your name: ")
    greet = f"Hello {user_name}!"
    Print(greet)

def Print(greet):
    print(greet)

PrintGreeting()
