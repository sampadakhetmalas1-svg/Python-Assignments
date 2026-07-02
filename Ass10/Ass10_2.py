#write program which accepts one number and print sum of first n natural numbers

num = int(input("Enter a number: "))

sum = 0
for i in range(1, num+1):
    sum = sum + i

print(sum)