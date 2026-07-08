#write lambda fun using filter() which accept list of number and return
#list of number divisible by 5 and 3

num = list(map(int,input("Enter numbers :").split()))

result = list(filter(lambda x: x%5 == 0 and x%3==0,num))

print("Number div by 3 and 5 are :",result)

