#write lambda fun using filter() which accept list of number and return
#count of even numbers

num = list(map(int,input("Enter numbers :").split()))

count = list(filter(lambda x :x%2==0,num))

print("Count of all even numbers is :",len(count))