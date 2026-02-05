# collections in python

# collections module: https://docs.python.org/3/library/collections.html

# https://www.youtube.com/watch?v=QswQA1lRIQY

###############################################################################################
# Counter: a dict subclass for counting hashable objects
###############################################################################################
from collections import Counter

print("\n############ Counter example ############\n")

# Example 1 usage of Counter
data = ['apple', 'banana', 'orange', 'apple', 'orange', 'apple']
fruit_counter = Counter(data)

print("Fruit counts:", fruit_counter)

# example 2 usage of Counter where list is a tuple of bigrams, add more tuples to see counts
bigrams = [('I', 'love'), ('love', 'coding'), ('I', 'love'), ('coding', 'is'), ('is', 'fun'), ('I', 'love'), ('love', 'coding'), ('coding', 'is')]
bigram_counter = Counter(bigrams)
print("Bigram counts:", bigram_counter)

###############################################################################################
# defaultdict: a dict subclass that calls a factory function to supply missing values
###############################################################################################
from collections import defaultdict

print("\n############ defaultdict example 1 ############\n")
# Example usage of defaultdict
word_to_length = defaultdict(lambda: 0)  # Default value for missing keys is 0
words = ['hello', 'world', 'python', 'collections']
for word in words:
    word_to_length[word] = len(word)

print("Word lengths:", word_to_length)


###############################################################################################
#  OrderedDict: a dict subclass that remembers the order entries were added                 ###
###############################################################################################
from collections import OrderedDict

print("\n############ OrderedDict example ############\n")
# Example usage of OrderedDict
ordered_dict = OrderedDict()
ordered_dict['first'] = 5
ordered_dict['second'] = 2
ordered_dict['third'] = 3

print("OrderedDict:", ordered_dict)
print("Keys in order:", list(ordered_dict.keys()))

###############################################################################################
#   namedtuple() returns a tuple with named value for each element in the tuple             ###
###############################################################################################

from collections import namedtuple

# Example usage of namedtuple
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(2, 3)
print("\n############ namedtuple example ############\n")
print("Point p1:", p1)
print("p1.x:", p1.x)
print("p1.y:", p1.y)

p2 = Point(5, 7)

sum = p1 + p2
print("Sum of p1 and p2: (wrong - works like concatenation)", sum)  # This will raise an error because namedtuples do not support addition by default.

# right way to add two namedtuples
sum_point = Point(p1.x + p2.x, p1.y + p2.y)
print("Sum of p1 and p2 (correct way):", sum_point)


###############################################################################################
#   deque: a list-like container with fast appends and pops on either end
###############################################################################################
from collections import deque

# Example usage of deque
print("\n############ deque example ############\n")
d = deque()
d.append('a')
d.append('b')
d.appendleft('z')
print("Deque after appends:", d)

d.pop()
print("Deque after pop:", d)


# Removing elements from both ends
d.popleft()
print("Deque after popleft:", d)
