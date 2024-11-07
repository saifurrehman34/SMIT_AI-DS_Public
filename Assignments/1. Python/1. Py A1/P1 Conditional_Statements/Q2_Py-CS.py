# Program to Determine if the User is a Minor, Adult, or Senior Citizen: This program takes the user's age as input and classifies them based on age groups.

age = int(input("Enter your age: "))

if age < 18:
    print(f"Congratulations! You are a minor because your age is {age}.")

elif 18 <= age < 50:
    print(f"Congratulations! You are an adult because your age is {age}.") 

else:
    print(f"Congratulations! You are a Senior Citizen because your age is {age}.")

