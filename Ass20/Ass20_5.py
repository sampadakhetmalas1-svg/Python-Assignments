# create 2 threads named thread1 and thread2
#Thread1 - display numbers 1 to 50
# Thread2 - display numbers 50 to 1 in reverse order
# Ensure that: Thread 2 starts execution only after thread1 has completed
# use appropriate thread syschronization


import threading

def thread1():
    for i in range(1, 51):
        print("Thread1:", i)

def thread2():
    for i in range(50, 0, -1):
        print("Thread2:", i)


t1 = threading.Thread(target=thread1, name="Thread1")
t2 = threading.Thread(target=thread2, name="Thread2")


t1.start()

# Wait for Thread1 to complete
t1.join()

# Start Thread2 after Thread1 finishes
t2.start()

# Wait for Thread2 to complete
t2.join()

print("Both threads completed")