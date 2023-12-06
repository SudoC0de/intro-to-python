# This program keeps asking for names, and for every name
# it prints out the number of characters in the name.
# Modify the code so it will exit if the user enters an empty string.

while True:
   name = input("Name: ")

   if len(name) == 0:
      break;
   else:
      print(f'{name} has {len(name)} characters.')