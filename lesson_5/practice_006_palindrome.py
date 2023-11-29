# A palindrome is a word, number, phrase, or other sequence of symbols
# that reads the same backwards as forwards:
#
# madam -> madam
# racecar -> racecar
# tacocat -> tacocat
#
# Write a program that will print True if the word is a palindrome
# and False if it is not.
string_check = input("Enter a string: ")

if string_check == string_check[::-1]:
    print("Palindrome: True")
else:
    print("Palindrome: False")
