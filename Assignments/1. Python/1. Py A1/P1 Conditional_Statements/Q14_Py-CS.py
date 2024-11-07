# Program to check if a year is a century year

# Input: year from the user
year = int(input("Enter a year: "))

# Check if the year is divisible by 100
if year % 100 == 0:
    print("It is a century year.")
else:
    print("It is not a century year.")
