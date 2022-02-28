# Created by vidit.singh at 28-02-2022

# List Comprehension

list1 = []  # Empty list

for item in 'Vidit':
    list1.append(item)
print(list1)

# Above can also be written as :

list2 = [item for item in 'Vidit']
print(list2)

# More
list3 = [temp for temp in range(1, 10)]
print(list3)  # Appends/Add the result to the list on each iteration.

list4 = [temp1 ** 2 for temp1 in range(1, 10) if temp1 % 2 == 0]
print(list4)  # Squares only even numbers.

list5 = [temp2 if temp2 % 2 == 0 else 'ODD' for temp2 in range(0, 10)]
print(list5)
