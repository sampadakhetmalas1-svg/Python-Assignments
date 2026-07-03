#Write program which accept one number and print reverse of that number

num = int(input("Enter Number :"))

def Reverse(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev

print("Reverse Num is : ",Reverse(num))
