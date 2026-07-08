#write program which contain one fun that accept one num from user
#  and returns true if div by 5 otherwise return false

def fun(num):
    return num % 5 == 0
    
num = int(input("Enter Number:"))

    
print(fun(num))