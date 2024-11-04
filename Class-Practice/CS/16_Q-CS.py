# Classifying a Triangle

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a == b == c:
    print("The triangle is Equilateral.")
elif a == b or b == c or a == c:
    print("The triangle is Isosceles.")
else:
    print("The triangle is Scalene.")
