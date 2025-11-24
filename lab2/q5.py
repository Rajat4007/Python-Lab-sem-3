# Student Name: Ankit Kumar
# Roll Number: 2024UG1034
# Course: CS-2101/CD-2101 - Python Programming Lab
# Experiment 2 - Task 5: Sales data & plotting

import matplotlib.pyplot as plt

sales_data = [25, 32, 29, 35, 41, 40, 45, 38, 50, 55, 60, 70]

total_sales = sum(sales_data)
avg_sales = total_sales / len(sales_data)
max_value = max(sales_data)
max_month = sales_data.index(max_value) + 1

print("Total Sales:", total_sales)
print("Average Sales:", avg_sales)
print("Highest Sales Month:", max_month)

months = list(range(1, 13))

plt.plot(months, sales_data, marker='o')
plt.scatter(max_month, max_value, s=200)
plt.xlabel("Month")
plt.ylabel("Sales (in thousands)")
plt.title("Monthly Sales Data")
plt.grid(True)
plt.show()
