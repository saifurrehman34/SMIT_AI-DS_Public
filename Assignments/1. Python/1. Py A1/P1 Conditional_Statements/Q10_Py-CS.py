# Program to determine if a character is a vowel or consonant

# Input: a single character from the user
char = input("Enter a character: ").lower()

# Check if the character is a vowel
if char in 'aeiou':
    print("The character is a vowel.")
else:
    print("The character is a consonant.")
