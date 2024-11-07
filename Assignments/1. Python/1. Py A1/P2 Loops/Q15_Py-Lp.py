# Print the sum of even and odd numbers separately up to a given number.

n = 10
even_sum = 0
odd_sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(f"Even Sum: {even_sum}")
print(f"Odd Sum: {odd_sum}")
