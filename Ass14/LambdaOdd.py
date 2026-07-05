#Write lambda fun which accepts one number and returns true if number is odd otherwise false

Odd = lambda n: n % 2 == 1

num = int(input("Enter a number: "))

print(Odd(num))