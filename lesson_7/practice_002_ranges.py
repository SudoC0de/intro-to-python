# Figure out the values required for range() to generate the expected result:

# 0, 1, 2, 3, 4
print(list(range(5)))

# 20, 21, 22 ... 30 (all the numbers between 20 and 30, inclusive)
print(list(range(20,31)))

# Even numbers: 2, 4, 6, 8, 10
print(list(range(2,11,2)))

# Years ending in zero between 1900 and 2000 (inclusive)
print(list(range(1900,2001,10)))

for year in range(1900,2001):
    if str(year).endswith("0"):
        print(year)

# Bonus!
# 20, 19, 18, 17, 16
print(list(range(20,15,-1)))