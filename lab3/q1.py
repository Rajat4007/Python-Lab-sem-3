# Student Name: Ankit Kumar
# Roll Number: 2024UG1034
# Course: CS-2101/CD-2101 - Python Programming Lab
# Experiment 3 - Task 1: Rectangle function

def rectangle_area_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

print(rectangle_area_perimeter(5, 3))
print(rectangle_area_perimeter(10, 4))
