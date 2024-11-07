# Program for a simple calculator

# Input: two numbers and an operator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

# Perform the calculation based on the operator
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:  # Check if the second number is not zero to avoid division by zero
        result = num1 / num2
    else:
        result = "Undefined (division by zero)"
else:
    result = "Invalid operator"

# Display the result
print("Result:", result)
