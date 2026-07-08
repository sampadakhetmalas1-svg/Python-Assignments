#accept one num and print pattern
# *   *   *
# *   *   
# *

def pattern():

    for i in range(num,0,-1):
        
        print("* "*i)




num = int(input("Enter number:"))
pattern()