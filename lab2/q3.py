# Student Name: Ankit Kumar
# Roll Number: 2024UG1034
# Course: CS-2101/CD-2101 - Python Programming Lab
# Experiment 2 - Task 3: Password validation

import re

while True:
    pwd = input("Enter a password: ")
    errors = []

    if len(pwd) < 8:
        errors.append("Minimum 8 characters required.")
    if not re.search(r"[A-Z]", pwd):
        errors.append("At least one uppercase letter required.")
    if not re.search(r"[a-z]", pwd):
        errors.append("At least one lowercase letter required.")
    if not re.search(r"[0-9]", pwd):
        errors.append("At least one number required.")
    if not re.search(r"[@#!$%^&*]", pwd):
        errors.append("At least one special character required (@,#,!, etc).")

    if len(errors) == 0:
        print("Password accepted!")
        break
    else:
        print("Invalid password:")
        for e in errors:
            print("-", e)
