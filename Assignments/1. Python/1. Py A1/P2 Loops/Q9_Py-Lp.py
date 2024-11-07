# Write a program to print the first 10 Fibonacci numbers.

# Starting values for the Fibonacci sequence
a, b = 0, 1

# We want to print the first 10 Fibonacci numbers
for step in range(10):
    # Print the current Fibonacci number (a)
    print(f"Step {step + 1}: Fibonacci number = {a}")
    
    # Print the current values of a and b (show how they change)
    print(f"    a = {a}, b = {b}")
    
    # Update a and b for the next step
    a, b = b, a + b
