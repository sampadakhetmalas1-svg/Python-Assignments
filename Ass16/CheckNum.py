#program which contain one fun named as chkNun().That fun which accept one parameter as number
#and find even and add num

def chkNum():
    num = int(input("Enter Number:"))

    if num%2 == 0:
        print (f"{num} is Even Number")

    else:
        print(f"{num} is odd number")

chkNum()
