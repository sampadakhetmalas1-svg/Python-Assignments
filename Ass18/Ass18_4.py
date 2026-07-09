# Write program which accept N numbers from user and stored it into list
# accept one another number from user and return frequency of that number from list

def Frequency(lst,num):
    count = 0
    for i in lst:
        if i == num:
            count = count + 1
    return count


def main():

    n = int(input("Enter number of elements :"))

    lst= list(map(int,input("Enter Elements :").split()))

    num = int(input("Enter number to find frequency :"))

    print("Frequency is :",Frequency(lst,num))

if __name__ == "__main__":
    main()