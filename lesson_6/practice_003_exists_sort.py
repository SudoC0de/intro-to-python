# Create a list that contains the ingredients for a sandwich. Yum.🥪
# If you want to use an empty list and add stuff to it, or start
# with a pre-populated list is up to you.

# Some people like cheese, some people don't. ONLY add cheese to your
# list of ingredients if you really like cheese.🧀

my_list = ['Bread', 'Ham', 'Cheese', 'Mayo', 'Lettuce', 'Onion', 'Banana Pepper']

# Then, use an if/else statement to print a message that will tell us
# whether you like cheese, based on its presence in the list.
if 'Cheese' in my_list:
    print('I like Cheese!')

# Then, to make it look pretty, sort the list in alphabetical order and print it out.
# Our computer is very old and it doesn't have a lot of memory. Also, we don't care
# about the original order of the ingredients.
my_list.sort()
print(my_list)
