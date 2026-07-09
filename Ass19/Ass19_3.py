#Write program which contain filter() , map(), reduce() in it.
# python application which contains one list of numbers,accept list from user
# using filter, filter out all num which >= 70 and <= 90.
# map will increase each num by 10
# reduce will return product of all that numbers
from functools import reduce

lst = list(map(int,input("Enter List of numbers :").split()))

print("List is :",lst)
fil = list(filter(lambda x:70 <= x <= 90,lst))

print("List after filter :",fil)

increase = list(map(lambda x:x+10,fil))

print("List After map:",increase)

product = reduce(lambda x,y:x*y,increase,0)

print("Product of all numbers is :",product)