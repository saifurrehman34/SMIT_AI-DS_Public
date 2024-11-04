# Checking String Case

user_string = input("Enter a string: ")

if user_string.isupper():
    print("The string is Uppercase.")
elif user_string.islower():
    print("The string is Lowercase.")
else:
    print("The string is Mixed case.")
