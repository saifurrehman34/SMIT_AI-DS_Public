# Sum of the Digits

number = input("Enter an integer: ")

# Calculate the sum of the digits
digit_sum = sum(int(digit) for digit in number if digit.isdigit())
print(f"The sum of the digits is: {digit_sum}")
