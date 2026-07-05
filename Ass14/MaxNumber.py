#Accept two number and return max number

Max = lambda No1,No2 : No1 if No1>No2 else No2

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Maximum number is :",Max(a,b))