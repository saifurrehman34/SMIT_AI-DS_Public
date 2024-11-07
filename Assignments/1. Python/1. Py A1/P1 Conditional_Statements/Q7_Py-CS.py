# Program to find the largest of three numbers

# Input: three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the largest number using nested if-else statements
if (num1 >= num2) and (num1 >= num3):
    print("The largest number is:", num1)
elif (num2 >= num1) and (num2 >= num3):
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)
