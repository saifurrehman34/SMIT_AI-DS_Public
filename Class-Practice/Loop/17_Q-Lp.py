# Number Guessing Game

correct_number = 7  # You can change this to any number
guess = None

while guess != correct_number:
    guess = int(input("Guess the number: "))

print("Congratulations! You guessed the correct number.")
