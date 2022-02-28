# Created by vidit.singh at 18-02-2022
# List in Python.

my_List = ['Vidit', 123, 12.12]
print(my_List)

# Indexing
print(my_List[0])
# Slicing
print(my_List[1:])  # Output : [123, 12.12]

# Concatenation
list1 = ['I', 'am']
list2 = ['Vidit', 'Singh']
print(list1 + list2)

# Add more elements
list1[0] = 'Hi'  # Replaces 0th element.
list1.append("ab")  # append element at end of the list.
print(list1)

# Removing items from list.
list1.pop()  # Removes the last element of a list.
print(list1)
list2.pop(0)  # Removes 0th position of list.
print(list2)

list3 = [6, 3, 9, 1, 8, 5]
list3.sort()
print(list3)

# ********************* Dictionaries **********************

dic = {'name': 'Vidit', 'age': 30}
print(dic['name'])

nested_dict = {'my_list': [1, 2, 3, 4, 5], 'n_dict': {'key1': 'Hello', 'key2': 'world!'}}

print(nested_dict['my_list'])
print(nested_dict['my_list'][2])

print(nested_dict['n_dict'])
print(nested_dict['n_dict']['key1'])

new_nested_list = {'key1': ["Vidit", "Kumar", 'Singh'], 'key2': {'m1': 2, 'm2': "Hi", 'm3': [3, 17, 8, 2, 9, 1]}}
print(new_nested_list['key1'][2].upper())  # Accessing element nested.

new_nested_list['key2']['m3'].sort()
print(new_nested_list['key2']['m3'])

new_nested_list['key3'] = 'Hello'

