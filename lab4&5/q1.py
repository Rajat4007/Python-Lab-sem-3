# Student Name: Ankit Kumar
# Roll Number: 2024UG1034
# Course: CS-2101/CD-2101 - Python Programming Lab
# Experiment 4 & 5 - Task 1: Writing & reading text file with exception handling

def write_students():
    try:
        with open(r"C:\Users\ankur\OneDrive\Desktop\Python lab\lab4&5\students.txt", "w") as f:
            f.write("Aman - A\n")
            f.write("Riya - B+\n")
            f.write("Sumit - A+\n")
            f.write("Khushi - B\n")
        print("students.txt created and data written successfully.")
    except PermissionError:
        print("Permission denied: Cannot write to the file.")
    except Exception as e:
        print("Error occurred:", e)

def read_students():
    try:
        with open(r"C:\Users\ankur\OneDrive\Desktop\Python lab\lab4&5\students.txt", "r") as f:
            print("\nContents of students.txt:")
            print(f.read())
    except FileNotFoundError:
        print("Error: students.txt not found.")
    except PermissionError:
        print("Permission denied: Cannot read the file.")
    except Exception as e:
        print("Error occurred:", e)

write_students()
read_students()
