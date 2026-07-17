#Write a program that calculates factorials of multiple numbers simultaneously
#  using multiprocessing.Pool.
#Input -Data [10, 15, 20, 25]
#Expected Task - For every N, calculate: N!
#Expected Output Format
#Process ID: 1240 Input Number: 20 Factorial 2432902008176640000

import os
import math
from multiprocessing import Pool

# Function to calculate factorial
def calculate_factorial(n):
    pid = os.getpid()
    fact = math.factorial(n)
    return f"Process ID: {pid} Input Number: {n} Factorial {fact}"

if __name__ == "__main__":
    # Input data
    data = [10, 15, 20, 25]

    # Create a pool of worker processes
    with Pool() as pool:
        results = pool.map(calculate_factorial, data)

    # Display results
    for result in results:
        print(result)