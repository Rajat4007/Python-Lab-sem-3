# Experiment 3 - Task 3: Day of week function

from datetime import datetime

def get_day_of_week(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return dt.strftime("%A")

print(get_day_of_week("2024-11-01"))
print(get_day_of_week("2025-01-01"))
