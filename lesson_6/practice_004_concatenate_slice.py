# For this exercise, you will create two lists. The first list will contain the work week days,
# the second list will contain the days of the weekend.
work_days = ['Monday','Tuesday','Wednesday','Thursday','Friday']
weekend_days = ['Saturday','Sunday']

# Then, you need to concatenate both lists into a third new list that represents the full week.
full_week = work_days + weekend_days

# Then, can you think of an easy way to create a new list that contains the days of two full weeks?
fortnight = full_week * 2

# Finally, once you have two full weeks into a list, use the slicer to:
# 1. Extract week 1 into its own list. Use this list in the next two points.
week_1 = fortnight[0:len(full_week):]

# 2. Write a slicer that will return the following: ['monday', 'wednesday', 'friday', 'sunday']
print(week_1[0::2])
