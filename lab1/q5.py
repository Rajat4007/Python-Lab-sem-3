# Student Name: Ankit Kumar
# Roll Number: 2024UG1034
# Course: CS-2101/CD-2101 - Python Programming Lab
# Experiment 1 - Task 5: Temperature conversion

choice = input("Convert (C)elsius to Fahrenheit or (F)ahrenheit to Celsius? ")

if choice.upper() == 'C':
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    print("Temperature in Fahrenheit:", f)

elif choice.upper() == 'F':
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print("Temperature in Celsius:", c)

else:
    print("Invalid choice!")
