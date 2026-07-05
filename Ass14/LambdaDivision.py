#Write lambda fun which accepts one number and returns true if number is divisible by 5 otherwise false

Div = lambda n: n % 5 == 0

num = int(input("Enter a number: "))

print(f"{num} is Divisible 5 ",(Div(num)))