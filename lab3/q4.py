# Experiment 3 - Task 4: Highest grade

def highest_grade(grades):
    return max(grades, key=grades.get)

students = {"Aman": 85, "Riya": 92, "Sumit": 88}
print("Top student:", highest_grade(students))
