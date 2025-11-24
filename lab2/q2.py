# Student Name: Ankit Kumar
# Roll Number: 2024UG1034
# Course: CS-2101/CD-2101 - Python Programming Lab
# Experiment 2 - Task 2: Multiplication table (1 to 12)

print("     MULTIPLICATION TABLE (1 to 12)\n")

print("     ", end="")
for col in range(1, 13):
    print(f"{col:4}", end="")
print()
print("-" * 60)

for row in range(1, 13):
    print(f"{row:4} |", end="")
    for col in range(1, 13):
        print(f"{row * col:4}", end="")
    print()
