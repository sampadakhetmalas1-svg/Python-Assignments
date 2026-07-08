#accept one num and print pattern
# 1
# 1 2 
# 1 2 3

def pattern():

    for i in range(1,num+1):
        for j in range(1,i+1):
            print(j,end=" ")
        
        print()




num = int(input("Enter number:"))
pattern()