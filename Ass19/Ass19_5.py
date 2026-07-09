#Write program which contain filter() , map(), reduce() in it.
# python application which contains one list of numbers,accept list from user
# using filter, filter out all num which are prime
# map fun will multiply each num by 2
# reduce will return max num frrom that numbers

from functools import reduce



def isPrime(num):
    if num <= 1:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True

def main():

    lst = list(map(int,input("Enter List of numbers :").split()))

    print("List is :",lst)

    prime = list(filter(isPrime, lst))
    print("Prime Numbers:", prime)

    # Multiply each prime number by 2
    modified = list(map(lambda x: x * 2, prime))
    print("After Map:", modified)

    # maximum 
    if modified:
        maximum = reduce(lambda x, y: x if x > y else y, modified)
        print("Maximum Number:", maximum)
    else:
        print("No prime numbers found.")

if __name__ == "__main__":
    main()