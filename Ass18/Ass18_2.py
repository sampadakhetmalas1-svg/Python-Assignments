#write program which accept N number from user and store it into list
# return maximum number from that list

from functools import reduce

num = list(map(int,input("Enter list of numbers :").split()))

max = reduce(lambda x,y:x if x>y else y,num)

print("Maximum of all numbers are :",max)