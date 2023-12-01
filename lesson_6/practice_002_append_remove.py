# Create an empty list and add the following elements about your location, in this order:
# - City
# - State or Province
# - A list with the temperatures the last three days
# - Your favorite animal

my_list = []
my_list.append('Grand Rapids')
my_list.append('Michigan')
my_list.append([32, 38, 25])
my_list.append('Monkey')

# Then, remove the State, without using the indexes.
my_list.remove('Michigan')

# Bonus: Remove the last element, using a negative index.
del my_list[-1]
