#write program which accept number from user and check whether that number is
#positive or negative or zero

def fun():

    num = int(input("Enter number :"))
    if num>0:
        print("Positive Number")

    elif num<0:
        print("Negative number")

    else:
        print("Zero")

fun()
