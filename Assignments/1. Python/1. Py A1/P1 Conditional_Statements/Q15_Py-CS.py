# Program to check if a number is within a specified range

# Input: number, lower limit, and upper limit from the user
num = float(input("Enter a number: "))
lower_limit = float(input("Enter the lower limit of the range: "))
upper_limit = float(input("Enter the upper limit of the range: "))

# Check if the number is within the range
if lower_limit <= num <= upper_limit:
    print("The number is within the range.")
else:
    print("The number is not within the range.")
