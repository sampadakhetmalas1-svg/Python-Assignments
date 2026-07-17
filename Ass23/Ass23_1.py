# Write program using multiprocessing.pool to calculate sum of all even numbers from 1 to N
# for every number from the given list
# Input - Data [1000000, 2000000, 3000000, 4000000]
#Expected Task - For each number N. calculate: 2+4+6+...+ N
#Expected Output Format -Process ID: 1234,Input Number: 1000000,Sum of Even Numbers: 250000500000

from multiprocessing import Pool
import os


def sum_even_numbers(n):
    # Sum of all even numbers from 1 to n
    even_sum = sum(i for i in range(2, n + 1, 2))

    return {
        "pid": os.getpid(),
        "input": n,
        "sum": even_sum
    }


def main():
    data = [1000000, 2000000, 3000000, 4000000]

    with Pool() as pool:
        results = pool.map(sum_even_numbers, data)

    for result in results:
        print(f"Process ID: {result['pid']}")
        print(f"Input Number: {result['input']}")
        print(f"Sum of Even Numbers: {result['sum']}")
        print("-" * 40)


if __name__ == "__main__":
    main()