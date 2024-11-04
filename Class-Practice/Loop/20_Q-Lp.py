# Countdown Timer

countdown_start = int(input("Enter a number to start the countdown: "))

print("Countdown:")
for number in range(countdown_start, -1, -1):
    print(number)
