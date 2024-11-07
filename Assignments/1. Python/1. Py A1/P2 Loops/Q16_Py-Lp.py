#  Create a program to calculate the sum of the digits of an inputted integer.

number = 1234
digit_sum = 0
while number > 0:
    digit_sum += number % 10
    number //= 10
print(digit_sum)
