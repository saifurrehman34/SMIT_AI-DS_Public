# Program to check if a number is a multiple of both 3 and 5

# Input: a number from the user
num = int(input("Enter a number: "))

# Check if the number is divisible by both 3 and 5
if (num % 3 == 0) and (num % 5 == 0):
    print("The number is a multiple of both 3 and 5.")
else:
    print("The number is not a multiple of both 3 and 5.")
