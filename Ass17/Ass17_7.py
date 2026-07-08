# accept input from user and print
# 1 2 3
# 1 2 3
# 1 2 3

def pattern():

    for i in range(num):
        for j in range(1,num+1):
            print(j,end=" ")
        
        print()




num = int(input("Enter number:"))
pattern()