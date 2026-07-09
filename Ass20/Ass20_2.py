# create 2 threads named as EvenFactor and OddFactor
# both thread should accept one integer number as parameter
# EvenFactor thread :- identify all even factors of the given number
#                    - calculate and display the sum of even factor
# OddFactor thread :- identify all odd factors of the given number
#                    - calculate and display the sum of odd factor
# after thread execution main thread should disp msg : "Exit from main"

import threading

def EvenFactor(num):
    even_factors = []

    for i in range(1, num + 1):
        if num % i == 0 and i % 2 == 0:
            even_factors.append(i)

    print("Even Factors:", even_factors)
    print("Sum of Even Factors:", sum(even_factors))



def OddFactor(num):
    odd_factors = []

    for i in range(1, num + 1):
        if num % i == 0 and i % 2 != 0:
            odd_factors.append(i)

    print("Odd Factors:", odd_factors)
    print("Sum of Odd Factors:", sum(odd_factors))



num = int(input("Enter a number: "))


even_thread = threading.Thread(target=EvenFactor,  args=(num,))
odd_thread = threading.Thread(target=OddFactor,  args=(num,))


even_thread.start()
odd_thread.start()


even_thread.join()
odd_thread.join()


print("Exit from main")