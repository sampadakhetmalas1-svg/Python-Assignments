# Write a program which accepts one number and check whether it is 
# divisible by 3 and 5 or not


num = int(input("Enter a number: "))

if(num%3 == 0 and num%5 == 0):
    print("Divisible by 3 and 5")

else:
    print("Not Divisible by 3 and 5")