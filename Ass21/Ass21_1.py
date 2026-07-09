#Create 2 threads named prime and non prime
#both threads accepts the list of integers
# prime thread should display all prime num from list
#Non prime display all non prime num from list

import threading

def isPrime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def prime(lst):
    prime_list = []

    for num in lst:
        if isPrime(num):
            prime_list.append(num)

    print("Prime Numbers:", prime_list)


def non_prime(lst):
    non_prime_list = []

    for num in lst:
        if not isPrime(num):
            non_prime_list.append(num)

    print("Non Prime Numbers:", non_prime_list)


# Accept list from user
lst = list(map(int, input("Enter list of numbers: ").split()))

# Create threads
t1 = threading.Thread(target=prime, name="prime", args=(lst,))
t2 = threading.Thread(target=non_prime, name="non prime", args=(lst,))

# Start threads
t1.start()
t2.start()

# Wait for completion
t1.join()
t2.join()

print("Both threads completed")