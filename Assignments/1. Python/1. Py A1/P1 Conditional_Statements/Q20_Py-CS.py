# Program to check if a number is prime

# Input: a positive integer from the user
num = int(input("Enter a positive integer: "))

# Initialize a flag variable to check if the number is prime
is_prime = True

# Prime numbers are greater than 1
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):  # Check factors up to the square root of num
        if num % i == 0:
            is_prime = False  # Set flag to False if a factor is found
            break

    if is_prime:
        print("The number is prime.")
    else:
        print("The number is not prime.")
else:
    print("The number is not prime (numbers less than 2 are not prime).")
