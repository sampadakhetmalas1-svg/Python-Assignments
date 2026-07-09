# creates 3 threds named small,Capital and Digits.
# All thred accept a string as input
# Small thread - count and display the number of lowercase characters
# Capital thread -count and display the number of uppercase characters
#Digit thread - count and display number of numeric digits
# each thread must also display - thread ID and Thread Name

import threading

def Small(s):
    count = 0
    for ch in s:
        if ch.islower():
            count += 1
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Lowercase characters:", count)

def Capital(s):
    count = 0
    for ch in s:
        if ch.isupper():
            count += 1
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Uppercase characters:", count)

def Digits(s):
    count = 0
    for ch in s:
        if ch.isdigit():
            count += 1
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Numeric digits:", count)

s = input("Enter a string: ")

t1 = threading.Thread(target=Small, args=(s,), name="Small")
t2 = threading.Thread(target=Capital, args=(s,), name="Capital")
t3 = threading.Thread(target=Digits, args=(s,), name="Digits")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("All threads completed")