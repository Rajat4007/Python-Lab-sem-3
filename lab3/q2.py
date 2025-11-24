# Experiment 3 - Task 2: List summary function

def list_summary(nums):
    total = sum(nums)
    avg = total / len(nums)
    max_val = max(nums)
    return total, avg, max_val

print(list_summary([5, 10, 15, 20, 25]))
