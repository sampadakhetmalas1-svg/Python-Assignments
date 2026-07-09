#write program which accept N number from user and store it into list
#returns the munimum element

from functools import reduce

num = list(map(int,input("Enter list of numbers :").split()))

min = reduce(lambda x,y:x if x<y else y,num)

print("Minimum of all numbers are :",min)