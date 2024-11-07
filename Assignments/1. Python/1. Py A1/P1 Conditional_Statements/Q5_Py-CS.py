# Program to convert grade percentage to letter grade

"""
Grade calculations as below
Above 90 = A
Above 80 = B
Above 60 = C
Above 40 = D
Below 40 = F

"""
percentage = float(input("Enter your grade percentage: "))

# Check if percentage is valid (between 0 and 100)
if percentage < 0 or percentage > 100:
    print(f"\nInvalid grade percentage.\n")
else:
    # Grade calculations
    if percentage >= 90:
        print(f"\nYou scored excellent, your grade is A.\n")
    elif percentage >= 80:
        print(f"\nYou scored good, your grade is B.\n")
    elif percentage >= 60:
        print(f"\nYou scored not bad, your grade is C.\n")
    elif percentage >= 40:
        print(f"\nYou scored poor, your grade is D.\n")
    else:
        print(f"\nYou scored very poor, your grade is F.\n")
