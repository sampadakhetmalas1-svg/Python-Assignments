#Write lambda fun which accepts one number and returns true if number is even otherwise false

even = lambda n: n % 2 == 0

num = int(input("Enter a number: "))

print(even(num))