# Print Numbers in Reverse Order
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Print numbers in reverse order
for number in range(end, start - 1, -1):
    print(number)
