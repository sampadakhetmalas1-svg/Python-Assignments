#Write program which contain filter() , map(), reduce() in it.
# python application which contains one list of numbers,accept list from user
# using filter, filter out all num which are even
# map fun will calculate its square
# reduce will return addition of  all that numbers

from functools import reduce

lst = list(map(int,input("Enter List of numbers :").split()))

print("List is :",lst)
even = list(filter(lambda x:x%2 ==0,lst))        #filter even number

print("List after filter :",even)

square = list(map(lambda x:x**2,even))

print("List After map:",square)

add = reduce(lambda x,y:x+y,square,0)

print("Addition of all numbers is :",add)