#write lambda fun using filter() which accepts a list of numbers
#and return odd numbers
 
num = list(map(int,input("Enter numbers : ").split()))

odd = list(filter(lambda x : x%2 != 0,num))

print("Odd Numbers are :",odd)