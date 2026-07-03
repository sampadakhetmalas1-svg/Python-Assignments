#Program  which accepts one number and print sum of Digits

num = int(input("Enter a number: "))



def sum_digits(num):
    sum = 0
    while num > 0:
        digit = num % 10        #get last digit
        sum = sum + digit
        num = num // 10
    return sum

print("Sum of digits =", sum_digits(num))