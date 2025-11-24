# Student Name: Ankit Kumar
# Roll Number: 2024UG1034
# Course: CS-2101/CD-2101 - Python Programming Lab
# Experiment 1 - Task 2: Student average & grade

m1 = float(input("Enter mark 1: "))
m2 = float(input("Enter mark 2: "))
m3 = float(input("Enter mark 3: "))

avg = (m1 + m2 + m3) / 3
print("Average =", avg)

if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Grade =", grade)
