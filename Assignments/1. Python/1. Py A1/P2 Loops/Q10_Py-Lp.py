# Use a loop to count the number of digits in an integer.

number = int(input("Enter a number: ")) 
count = 0 

while number > 0:
    count += 1       # Increment the count for each digit
    number //= 10    # Remove the last digit by integer division

print("The number of digits is:", count)

