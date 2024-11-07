# Program to check if the temperature is freezing, moderate, or hot

# Input: temperature in Celsius
temperature = float(input("Enter the temperature in Celsius: "))

# Determine the temperature status based on Celsius value
if temperature <= 0:
    print("It's freezing.")
elif 1 <= temperature <= 30:
    print("It's moderate.")
else:
    print("It's hot.")
