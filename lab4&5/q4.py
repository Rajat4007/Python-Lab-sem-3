# Student Name: Ankit Kumar
# Roll Number: 2024UG1034
# Course: CS-2101/CD-2101 - Python Programming Lab
# Experiment 4 & 5 - Task 4: Copy file contents

def copy_file():
    try:
        with open(r"C:\Users\ankur\OneDrive\Desktop\Python lab\lab4&5\source.txt", "r") as src:
            data = src.read()
        with open(r"C:\Users\ankur\OneDrive\Desktop\Python lab\lab4&5\destination.txt", "w") as dest:
            dest.write(data)

        print("File copied successfully.")
    except FileNotFoundError:
        print("source.txt not found.")
    except PermissionError:
        print("Permission error.")
    except Exception as e:
        print("Error occurred:", e)

copy_file()
