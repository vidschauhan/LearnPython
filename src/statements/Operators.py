# Created by vidit.singh at 28-02-2022

# Range Operator.

for items in range(10):
    print(items)  # Prints 0 to 9

for items in range(5, 10):
    print(items)  # Prints 5 to 9 excludes 10.

for items in range(1, 10, 2):
    print(items)  # Starts with 1 to 10 (excludes 10) with increment of 2

# To keep track of index.
index = 0
for item in 'Vidit':
    print(f'Word at index {index} is {item}')
    index += 1

index_count, word = 0, 'Vidit'
for item in word:
    print(word[index_count])
    index_count += 1

# enumerate help to get the index and char as tuple.
name = 'Hello'
for t in enumerate(name):
    print(t)  # Returns tuple with index and char at that index. (0, 'H')

for idx, ch in enumerate(name):
    print(idx)  # Returns all the index
    print(ch, '\n')  # Returns all the char at that index.

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [12, 34, 5, 3, 12]

for it in zip(list1, list2, list3):
    print(it)  # Zips two lists and returns tuples. If the size of the list is uneven then,
    # it picks the smallest list to zip and ignores rest of other list elements.

# In keyword

print('V' in 'Vidit')
print('a' in ['a', 'b', 'c'])
print('key' in {'Key': 1, 'Key2': 2})
dic = {'Key': 12, 'Key2': 21}
print(12 in dic.values())

# Importing a libraries
from random import shuffle, randint

shuffle(list3)  # Importing only shuffle function from random class. Shuffles list3.
print(list3)
print(randint(1, 100))

my_num = input("Please enter a number : ")  # Input always accept as string. Typecast before use.
print(type(my_num))

v = int(my_num)  # Converts string to int.
print(type(v))

num = int(input("Please enter a number : "))  # Takes string input and convert to int.
print(type(num))
