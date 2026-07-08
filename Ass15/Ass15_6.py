##write lambda fun using reduce() which accepts list of number and return
#returns the munimum element

from functools import reduce

num = list(map(int,input("Enter list of numbers :").split()))

min = reduce(lambda x,y:x if x<y else y,num)

print("Minimum of all numbers are :",min)