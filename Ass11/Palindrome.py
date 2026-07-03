#Accept one number and Check whether it is palindrome or not

num = int(input("Enter Number :"))

def Palindrome(num):

    original = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    
    if original == rev:
        print("Palindrome Number")

    else:
        print("Not a Palindrome Number")


Palindrome(num)

