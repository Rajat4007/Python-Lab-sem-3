# Student Name: Ankit Kumar
# Roll Number: 2024UG1034
# Course: CS-2101/CD-2101 - Python Programming Lab
# Experiment 2 - Task 1: Age classification

age_input = input("Enter your age: ")

if age_input.isdigit():
    age = int(age_input)

    if age < 18:
        print("You are a minor.")
    elif 18 <= age <= 65:
        print("You are an adult.")
    else:
        print("You are a senior.")
else:
    print("Invalid input! Please enter a number.")
