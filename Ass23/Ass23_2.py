#Write a Python program using multiprocessing. Pool to calculate the sum of 
# all odd numbers from 1 to N.
#Input -Data [1000000, 2000000, 3000000, 4000000]
#Expected Task - For each number N, calculate: 1+3+5+....+ N
#Expected Output Format - Process ID: 1235
#Input Number: 1000000 Sum of Odd Numbers 250000000000

from multiprocessing import Pool
import os


def sum_odd_numbers(n):
    # Sum of all odd numbers from 1 to n
    odd_sum = sum(i for i in range(1, n + 1, 2))

    return {
        "pid": os.getpid(),
        "input": n,
        "sum": odd_sum
    }


def main():
    data = [1000000, 2000000, 3000000, 4000000]

    # Create a pool of worker processes
    with Pool() as pool:
        results = pool.map(sum_odd_numbers, data)

    # Display results
    for result in results:
        print(f"Process ID: {result['pid']}")
        print(f"Input Number: {result['input']}")
        print(f"Sum of Odd Numbers: {result['sum']}")
        print("-" * 40)


if __name__ == "__main__":
    main()