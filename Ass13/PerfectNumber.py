#Accept one number and check whether it is prefect number or not
#(Sum of all its proper divisiors 6 → 1 + 2 + 3 = 6 )

Num = int(input("Enter Number :"))

def PerfectNumber(Num):

    sum = 0

    for i in range(1, Num):
        if Num % i == 0:
            sum = sum + i

    if sum == Num:
        print("Perfect Number")

    else:
        print("Not Perfect Number")


PerfectNumber(Num)

