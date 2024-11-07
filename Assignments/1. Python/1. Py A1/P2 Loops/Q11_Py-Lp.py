# Print the reverse of a given number.

# Take input from the user
number = int(input("Enter a number: "))
reverse = 0 

print(f"Initial number: {number}")

# While loop to reverse the digits
while number > 0:
    last_digit = number % 10 
    reverse = reverse * 10 + last_digit 
    number //= 10
    
    # Print the current state after each iteration
    print(f"Current number: {number}, Last digit: {last_digit}, Reversed so far: {reverse}")

print(f"Reversed number: {reverse}")
