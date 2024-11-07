# Python Program to Check for Leap Year
# Using variables, operators, and conditional statements

# Get input from user

year = int(input("Enter a year to check if it's a leap year: "))

# Print the year we're checking
print(f"\nChecking if {year} is a leap year...")

if (year % 400 == 0) and (year % 100 == 0):
    print(f"\nResult: {year} is a LEAP Year.")

elif(year % 4 == 0) and (year % 100 != 0):
    print(f"\nResult: {year} is a LEAP Year.")
else:
    print(f"\nResult: {year} is not a LEAP Year. Because {year} is a NORMAL Year.")
    