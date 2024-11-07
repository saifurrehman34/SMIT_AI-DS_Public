# Program to check if a string is uppercase, lowercase, or mixed

# Input: a string from the user
text = input("Enter a string: ")

# Check the case of the string
if text.isupper():
    print("The string is in uppercase.")
elif text.islower():
    print("The string is in lowercase.")
else:
    print("The string is a mix of uppercase and lowercase.")
