#write programe which aceept one number and check whether the number is prime or not

num = int(input("Enter a number: "))

count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count = count + 1

if count == 2:
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")
