# Given two words, check if both are anagrams.
# An anagram of a string is another string that contains the same characters, only the order
# of characters can be different.
# For example:
# is_anagram('cat', 'act') => should return True
# is_anagram('bus', 'sub') => should return True
# is_anagram('map', 'cap') => should return False
word1 = "cat"
word2 = "tac"

if len(word1) == len(word2):
    if sorted(word1) == sorted(word2):
        print("True")
    else:
        print("False")
else:
    print("False")
