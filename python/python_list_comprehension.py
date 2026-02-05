print("\n############ loop without list comprehension ############\n")

nums = [1, 2, 3, 4, 5]
squared = []
for num in nums:
    squared.append(num ** 2)

print("Squared numbers (without list comprehension):", squared)

print("\n############ loop with list comprehension ############\n")

num_squared = [num ** 2 for num in nums]
print("Squared numbers (with list comprehension):", num_squared)

print("\n############ list comprehension with condition ############\n")
even_squared = [num ** 2 for num in nums if num % 2 == 0]
print("Squared even numbers (with condition):", even_squared)

print("\n############ nested loop with list comprehension ############\n")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Flattened matrix (with nested list comprehension):", flattened)

print("\n############ list comprehension with function call ############\n")
def square(x):
    return x ** 2

squared_with_func = [square(num) for num in nums]
print("Squared numbers (with function call):", squared_with_func)

print("\n############ list comprehension with string manipulation ############\n")
words = ['hello', 'world', 'python', 'list', 'comprehension']
uppercased = [word.upper() for word in words]
print("Uppercased words (with list comprehension):", uppercased)

print("\n############ list comprehension with tuple unpacking ############\n")
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
numbers = [num for num, word in pairs]
print("Numbers extracted from pairs (with tuple unpacking):", numbers)

print("\n############ show performance gain using list comprehension ############\n")
import time
from tracemalloc import start

start_time = time.time()
squared_loop = []
for num in range(1000000):
    squared_loop.append(num ** 2)
end_time = time.time()
print("Time taken with loop: {:.5f} seconds".format(end_time - start_time))

start_time = time.time()
squared_list_comp = [num ** 2 for num in range(1000000)]
end_time = time.time()
print("Time taken with list comprehension: {:.5f} seconds".format(end_time - start_time))

print("\n")