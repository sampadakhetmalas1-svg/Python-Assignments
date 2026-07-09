# create 2 threads
# thread 1 should comput the sum of elements from a list
# thread 2 should compute product of elements from the same list
# return the result to the main thread and display them

import threading

lst = [1, 2, 3, 4, 5]

sum_result = 0
product_result = 1

def calculate_sum():
    global sum_result

    for num in lst:
        sum_result += num


def calculate_product():
    global product_result

    for num in lst:
        product_result *= num


t1 = threading.Thread(target=calculate_sum)
t2 = threading.Thread(target=calculate_product)


t1.start()
t2.start()


t1.join()
t2.join()


print("List:", lst)
print("Sum of elements:", sum_result)
print("Product of elements:", product_result)