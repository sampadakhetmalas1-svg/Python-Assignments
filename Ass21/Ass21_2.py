#Create 2 threads
# thread 1 should calculate and display maximunm element from an list
# thread 2 should calculate and display minimunm element from same list
#the list should be accepted from the user


import threading


def find_max(numbers):
    maximum = max(numbers)
    print("Maximum element:", maximum)


def find_min(numbers):
    minimum = min(numbers)
    print("Minimum element:", minimum)


numbers = list(map(int, input("Enter list elements separated by spaces: ").split()))


thread1 = threading.Thread(target=find_max, args=(numbers,))
thread2 = threading.Thread(target=find_min, args=(numbers,))


thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("Both threads have completed execution.")