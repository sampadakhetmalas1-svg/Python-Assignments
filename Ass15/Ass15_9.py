#write lambda fun using reduce() which accepts a list of numbrs and return
#product of all elements

from functools import reduce

num = list(map(int,input("Enter list of numbers :").split()))

product = reduce(lambda x,y:x*y,num)

print("Product of all numbers are :",product)