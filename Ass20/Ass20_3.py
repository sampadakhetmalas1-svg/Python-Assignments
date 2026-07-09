# create 2 threads named as EvenList and OddList
#Both threads should accepts list of integers as input
# the evenList thread should - extract all even elements from list, 
#                             - calculate and display their sum
# the oddList thread  should - extract all odd elements from list, 
#                             - calculate and display their sum
#Thread should run concurrently

import threading

def EvenList(lst):
    even = []
    s = 0
    for i in lst:
        if i % 2 == 0:
            even.append(i)
            s = s + i
    print("Even elements:", even)
    print("Even sum:", s)

def OddList(lst):
    odd = []
    s = 0
    for i in lst:
        if i % 2 != 0:
            odd.append(i)
            s = s + i
    print("Odd elements:", odd)
    print("Odd sum:", s)

lst = list(map(int, input("Enter list elements: ").split()))

t1 = threading.Thread(target=EvenList, args=(lst,), name="EvenList")
t2 = threading.Thread(target=OddList, args=(lst,), name="OddList")

t1.start()
t2.start()

t1.join()
t2.join()

print("Execution completed")