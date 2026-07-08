#accept num from user and return addition of digits in that number

def fun():
    num = int(input("Enter number: "))

    sum = 0
    while num!= 0:
        sum = sum + (num%10)
        num = num // 10
    print("Addition of digits in this number are :",sum)

fun()