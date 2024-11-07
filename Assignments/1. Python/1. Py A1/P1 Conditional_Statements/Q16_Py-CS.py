# Program to classify a triangle as equilateral, isosceles, or scalene

# Input: three sides of a triangle
side1 = float(input("Enter the first side length: "))
side2 = float(input("Enter the second side length: "))
side3 = float(input("Enter the third side length: "))

# Classify the triangle based on the sides
if side1 == side2 == side3:
    print("The triangle is equilateral (all sides are equal).")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is isosceles (two sides are equal).")
else:
    print("The triangle is scalene (all sides are different).")
