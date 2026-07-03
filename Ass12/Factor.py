# Accept number and print factors of that number

num = int(input("Enter a number: "))


for i in range(1, num + 1):
    if num % i == 0:
        print(i)

print("Factors of", num, "are:")