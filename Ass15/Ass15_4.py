#write lambda fun using reduce() which accepts list of number and return
#addition of  all elements

from functools import reduce


num = list(map(int,input("Enter list of numbers :").split()))

addition = reduce(lambda x,y:x+y,num)

print("Addition of all numbers are :",addition)