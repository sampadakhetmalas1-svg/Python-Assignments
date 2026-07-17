#Write a program that counts how many odd numbers exist between 1 and N.
#Input - Data [1000000, 2000000, 3000000, 4000000]
#Expected Output Format
#Process ID: 1237 ,Input Number: 1000000, Odd Number Count: 500000


import os

# Input data
data = [1000000, 2000000, 3000000, 4000000]

# Get current process ID
pid = os.getpid()

# Count odd numbers from 1 to N
for n in data:
    odd_count = (n + 1) // 2
    print(f"Process ID: {pid}, Input Number: {n}, Odd Number Count: {odd_count}")