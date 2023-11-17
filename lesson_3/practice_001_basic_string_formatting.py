# Given the following variables:
name = "Emily"
age = 26
job_title = "QA Manager"

# For each practice, print the following message using
# the requested string formatting method:
# "Emily is a 26 years old QA manager of our company"

# Practice 1.1 - Using concatenation with +
# (your solution goes here)
print(name + ' is a ' + str(age) + ' years old ' + job_title + ' of our company')

# Practice 1.2 - Using .format()
# (your solution goes here)
print('{0} is a {1} years old {2} of our company'.format(name, age, job_title))

# Practice 1.3 - Using f-strings
# (your solution goes here)
print(f'{name} is a {age} years old {job_title} of our company')
