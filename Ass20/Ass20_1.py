#create 2 separate threads named even and odd
# even display first 10 even numbers
#odd display first 10 odd numbers
# both thread should execute independently using the threading module
# ensure proper thread creation and execution

import threading


def even():
    print("Even Thread:")
    for i in range(2, 21, 2):
        print(i)


def odd():
    print("Odd Thread:")
    for i in range(1, 20, 2):
        print(i)


even_thread = threading.Thread(target=even, name="even")
odd_thread = threading.Thread(target=odd, name="odd")


even_thread.start()
odd_thread.start()


even_thread.join()
odd_thread.join()

print("Both threads execution completed.")