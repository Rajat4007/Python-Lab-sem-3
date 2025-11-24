# Student Name: Ankit Kumar
# Roll Number: 2024UG1034
# Course: CS-2101/CD-2101 - Python Programming Lab
# Experiment 4 & 5 - Task 2: Day of week from date

from datetime import datetime

def get_day_of_week(date_string):
    try:
        date_obj = datetime.strptime(date_string, "%Y-%m-%d")
        return date_obj.strftime("%A")
    except ValueError:
        return "Invalid date format! Use YYYY-MM-DD."

# Testing with different dates
print(get_day_of_week("2025-11-24"))
print(get_day_of_week("2024-01-01"))
print(get_day_of_week("2023-08-15"))
