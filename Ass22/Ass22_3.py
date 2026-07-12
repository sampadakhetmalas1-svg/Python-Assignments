# For every number in the given list, count how many prime numbers
#  exists between 1 and N using multiprocessing pool.
# Display total count for eact number

from multiprocessing import Pool

def Prime(n):
    if n<2 :
        return False
    
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def countPrime(n):
    count = 0
    for i in range(1,n+1):
        if Prime(i):
            count += 1
    return count

def main():
    num = [10000, 20000, 30000, 40000]

    with Pool() as p:
        result = p.map(countPrime,num)

    print(result)

if __name__ == "__main__":  
    main()