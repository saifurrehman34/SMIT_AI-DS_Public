# Find the factorial of a number using a while loop.

# Take input from the user
number = int(input("Enter a number to calculate its factorial: "))

# Initialize variables
factorial = 1
i = 1

# Start the calculation and print the process step-by-step
print(f"Calculating the factorial of {number}:")
while i <= number:
    # Show the current step
    print(f"Step {i}: factorial = {factorial} * {i} = {factorial * i}")
    
    # Update factorial and increment the counter
    factorial *= i
    i += 1

# Final result
print(f"\nThe factorial of {number} is {factorial}\n")

