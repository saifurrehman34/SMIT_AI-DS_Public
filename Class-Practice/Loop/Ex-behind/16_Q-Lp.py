number = input("Enter your string: ")
digit_sum = 0  # Initialize the sum

# Print the original number
print(f"\nOriginal string: '{number}'\n")

# Use a list to keep track of the digits found
digits_found = []

# Iterate over each character in the string
for digit in number:
    # Check if the character is a digit
    if digit.isdigit():
        # Convert the character to an integer
        digit_value = int(digit)
        # Add the digit to the sum
        digit_sum += digit_value
        # Store the found digit
        digits_found.append(digit_value)
        # Print the current digit and updated sum
        print(f"Found digit: {digit} (value: {digit_value}), current sum: {digit_sum}")
    else:
        # Print that the character is skipped
        print(f"Skipped character: '{digit}'")

# Final output
print(f"\nThe sum of the digits in '{number}' is: {digit_sum}")
print(f"Digits found: {digits_found}")
