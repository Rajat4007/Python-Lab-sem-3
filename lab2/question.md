○ Task 1: Create a Python program that asks the user for their age. Implement conditional statements to check the following: If the user is below 18, print "You are a minor." If the user is between 18 and 65, print "You are an adult." If the user is above 65, print "You are a senior." Add a check for invalid input (e.g., user enters a non-numeric value). 

○ Task 2: Write a Python program that generates a multiplication table for numbers from 1 to 12. Use nested loops to display the table in a well-formatted way. Print both the rows and columns of the table with their appropriate labels. 

○ Task 3: Write a program to validate a password based on the following criteria: 
■ Minimum 8 characters 
■ At least one uppercase letter 
■ At least one lowercase letter 
■ At least one number 
■ At least one special character (e.g., @, #, !, etc.) 

Use a while loop to repeatedly ask for a password until a valid one is entered. Use decision-making to give feedback to the user about which criteria were not met.

○ Task 4: Create a complex, nested dictionary representing IIIT Ranchi’s organizational structure. (Visit:https://iiitranchi.ac.in/organizational_structure.aspx). 

Write a Python program that accepts the name of an Assistant Professor and iterates through the dictionary to search for that professor. If the name is found, print the department they belong to. If the name is not found at the current level, continue to the next level of the dictionary. If the name is not found in the entire structure, display a message indicating that the Assistant Professor was not found.


○ Task 5: Create a list of sales data for the past 12 months (e.g., sales figures in thousands). Calculate the total sales, average sales, and the month with the highest sales using loops. Use matplotlib to plot the monthly sales and highlight the month with the highest sales. 

Example: # Sales data (in thousands) 
sales_data = [25, 32, 29, 35, 41, 40, 45, 38, 50, 55, 60, 70]

### Python String Formatting with `f"{col:4}"`

In the multiplication table code, `f"{col:4}"` is an example of Python's **formatted string literal** (f-string). Here's what it means:

- `f"..."` enables embedding expressions directly inside string literals.
- `{col}` refers to the variable whose value will be printed.
- `:4` is a **format specifier** that sets the field width to 4 characters, ensuring proper alignment in tabular output.

This formatting helps maintain a clean and readable structure, especially when printing numbers in rows and columns. For example, `f"{7:4}"` will output `'   7'`, aligning the number to the right within a 4-character space.

### Python `print()` with `end` Parameter

In Python, the `print()` function adds a newline (`\n`) by default after each output. To change this behavior, we use the `end` parameter.

- `end=" "` replaces the default newline with a space.
- `end=""` prints output without any space or newline.
- This is useful when printing multiple items on the same line, such as in loops or formatted tables.

**Example:**
```python
for i in range(1, 4):
    print(i, end=" ")

 Output: 1 2 3

