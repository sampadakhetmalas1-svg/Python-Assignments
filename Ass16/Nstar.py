#write program which accept number from user and print that number of "*"
# on screen

def fun(num):

    for i in range(1,num+1,1):
        print("*")

num = int(input("Enter Number :"))
fun(num)