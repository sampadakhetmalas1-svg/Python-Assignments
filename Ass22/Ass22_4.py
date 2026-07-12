# write program that calculates 1^5 + 2^5 + 3^5....+N^5
#for multiple values of N simultaneously using pool
# input [1000000,2000000,3000000,4000000] measure total execution time


from multiprocessing import Pool
import time


def sum_of_fifth_powers(n):
    
    return sum(i**5 for i in range(1, n + 1))


def main():
    inputs = [1000000, 2000000, 3000000, 4000000]

    start_time = time.perf_counter()

    # Create a pool 
    with Pool() as pool:
        results = pool.map(sum_of_fifth_powers, inputs)

    end_time = time.perf_counter()

    # Display results
    for n, result in zip(inputs, results):
        print(f"Sum of fifth powers up to {n} = {result}")

    print(f"\nTotal execution time: {end_time - start_time:.4f} seconds")


if __name__ == "__main__":
    main()