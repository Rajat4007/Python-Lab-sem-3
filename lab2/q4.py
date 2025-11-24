# Student Name: Ankit Kumar
# Roll Number: 2024UG1034
# Course: CS-2101/CD-2101 - Python Programming Lab
# Experiment 2 - Task 4: Search faculty in nested IIIT Ranchi structure

iiit_ranchi = {
    "Departments": {
        "CSE": {
            "Assistant Professors": ["Dr. N Kishor", "Dr. B Singh","Dr. Nitika"]
        },
        "ECE": {
            "Assistant Professors": ["Dr. Ravi Shankar", "Dr. Priyabharat"]
        }
    }
}

name = input("Enter Assistant Professor name: ")
found = False

for dept, data in iiit_ranchi["Departments"].items():
    if name in data["Assistant Professors"]:
        print(name, "belongs to", dept)
        found = True
        break

if not found:
    print("Assistant Professor not found.")
