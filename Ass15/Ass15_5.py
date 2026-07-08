##write lambda fun using reduce() which accepts list of number and return
#returns the maximum element

from functools import reduce

num = list(map(int,input("Enter list of numbers :").split()))

max = reduce(lambda x,y:x if x>y else y,num)

print("Maximum of all numbers are :",max)