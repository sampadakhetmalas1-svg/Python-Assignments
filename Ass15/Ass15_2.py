#write lambda fun using filter() which accepts a list of numbers
#and return even numbers
 
num = list(map(int,input("Enter list of Numbers :").split()))

even = list(filter(lambda x : x%2 ==0,num))

print("Even numbers are :",even)