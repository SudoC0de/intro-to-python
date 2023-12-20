# Create a program, that takes a word input from the user, and prints out a
# dictionary showing the letter count for each letter in the word.

# Examples:
#   cat  -> {"c" : 1, "a" : 1, "t" : 1}
#   call -> {"c" : 1, "a" : 1, "l" : 2}

# Use as many of the following concepts as you can:
# - Functions
# - Dictionaries
# - Asking for user input
# - Loops

# Bonus: Keep asking for words until the user types "end" OR an empty word.
def word_input():
    letter_count = {}

    while True:
        word = input("Input (\"End\" to quit): ")

        if word == "End":
            break
        else:
            for letter in set(word):
                letter_count.update({(letter, word.count(letter))})

            print(letter_count)
            letter_count = {}

word_input()
