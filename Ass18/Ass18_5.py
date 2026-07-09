## Write program which accept N numbers from user and stored it into list
# return addition of all prime numbers from that list.
#main python file accepts N number to checkprime() fun 
# which is part of our user defined module named as MarvellousNum.
# name of fun from main python file should be ListPrime()


import MarvellousNum
def ListPrime(lst):
    sum = 0

    for i in lst:
        if MarvellousNum.CheckPrime(i):
            sum = sum + i
            
    return sum 


def main():
    n= int(input("Enter Number of elements :"))

    lst = list(map(int,input("Enter elements :").split()))
    
    print("Addition of prime numbers is :",ListPrime(lst))




if __name__ == "__main__":
    main()