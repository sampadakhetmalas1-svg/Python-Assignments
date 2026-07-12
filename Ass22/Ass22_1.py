# Accept list of integers and uses Pool.map() to calculate 
# the sum of squares from 1 to N for every element in list

from multiprocessing import Pool

def Sum_of_squares(n):
    return n * (n+1) * (2 * n + 1)//6       # formula to find sum of squares


def main():

    numbers = list(map(int,input("Enter numbers :").split()))

    with Pool() as p:
        result = p.map(Sum_of_squares,numbers)
        print(result)

if __name__ == "__main__":
    main()
