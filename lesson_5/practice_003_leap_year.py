# Your goal is to decide if a given year is a leap year.
# A leap year is divisible by 4, except for centuries (divisible by 100)
# which must also be divisible by 400.

year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")