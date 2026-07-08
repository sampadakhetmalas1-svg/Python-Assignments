#Write lambda fun using map() which accepts list of numbers and returns 
# a list of squares of each num


num = list(map(int,input("Enter List : ").split()))

Square = list(map(lambda x: x*x,num))

print("Squares of all numbers are :",Square)





