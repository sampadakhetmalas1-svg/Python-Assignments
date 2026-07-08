#write lambda fun using filter() which accept list of strings and return
#list of string having length greater than 5

name = list(input("Enter names :").split())

result = list(filter(lambda x: len(x)>5,name))

print(result)