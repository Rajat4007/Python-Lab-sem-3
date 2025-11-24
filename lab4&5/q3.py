# Student Name: Ankit Kumar
# Roll Number: 2024UG1034
# Course: CS-2101/CD-2101 - Python Programming Lab
# Experiment 4 & 5 - Task 3: Counting lines, words and characters

def count_file_data():
    try:
        with open(r"C:\Users\ankur\OneDrive\Desktop\Python lab\lab4&5\sample.txt", "r") as f:
            data = f.read()

            lines = data.split("\n")
            words = data.split()
            characters = len(data)

            print("File Statistics:")
            print("Total Lines     :", len(lines))
            print("Total Words     :", len(words))
            print("Total Characters:", characters)
    except FileNotFoundError:
        print("sample.txt not found.")
    except Exception as e:
        print("Error occurred:", e)

count_file_data()
