# Experiment 3 - Task 5: Random prime check

import random
import math

num = random.randint(1, 100)
print("Random number:", num)

if num > 1:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")
