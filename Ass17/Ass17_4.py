#write program which accept one number from user and return addition of its factors

def Addfactors():

    num = int(input("Enter a number: "))

    sum = 0
    for i in range(1, num+1):
        sum = sum + i

    print(sum)

Addfactors()