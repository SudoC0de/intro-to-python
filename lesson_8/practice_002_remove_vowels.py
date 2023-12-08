# Remove the lowercase vowels in a given string:
# str1 = ‘Hello, World!’
# The vowels are:
# vowels = "aeiou"
# “y” is not considered a vowel for this task. The input string is always in lowercase.
# Examples:
# "hello" --> "hll"
# "goodbye" --> "gdby"
string1 = "Hello World!"
lower_vowels = "aeiou"
answer = ""

for character in string1:
    if character not in lower_vowels:
        answer += character

print(answer)
