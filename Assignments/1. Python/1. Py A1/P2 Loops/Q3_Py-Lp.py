# Write a program to calculate the sum of all numbers between 1 and 100.

sum = 0
for i in range(1, 101):
    sum += i
    print(f"After adding {i}, the sum is now {sum}")