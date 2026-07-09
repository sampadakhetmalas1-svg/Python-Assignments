# write program which accept N number from user and store it into list
# return addition of all element from that list

from functools import reduce


num = list(map(int,input("Enter list of numbers :").split()))

addition = reduce(lambda x,y:x+y,num)

print("Addition of all numbers are :",addition)
