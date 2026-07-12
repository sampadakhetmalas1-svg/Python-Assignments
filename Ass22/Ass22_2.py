# write program that calculate factorials of multiple numbers simultaneously
# using Pool.map() : process ID, Input number, Factorial

from multiprocessing import Pool
import os
import math

def Fact_info(n):
    return (os.getpid(), n , math.factorial(n))

def main():
    num = [10,15,20,25]

    with Pool() as p:
        result = p.map(Fact_info, num)
        print("Process Id \t Input Number \t Factorial")
        for pid, num, fact in result:
            print(f"{pid}\t\t{num}\t\t{fact}")

if __name__ == "__main__":
    main()