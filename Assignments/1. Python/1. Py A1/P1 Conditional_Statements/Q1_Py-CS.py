# Program to Check if a Number is Positive, Negative, or Zero: This program takes a number from the user and checks if it's positive, negative, or zero.


number = int(input("Enter a number: "))

if number > 0:
    print(f"The number {number} is positive.")

elif number < 0:
    print(f"The number {number} is negative.")

else:
    print(f"The number {number} is zero.")