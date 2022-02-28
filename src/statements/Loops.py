# Created by vidit.singh at 28-02-2022

# For Loop
my_List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for m in my_List:
    if m % 2 == 0:
        print(m)

my_str = 'Hello'
for str1 in my_str:
    print(str1)

for gg in my_str:
    print("Vidit")

for _ in my_str:
    print("Singh")

for m in my_str:
    pass

# Iterating over tuple
tup_list = [(1, 2), (3, 4), (5, 6)]
for item in tup_list:
    print(item)

# Tuple unpacking
for a, b in tup_list:
    print(b)

# iterating over Dictionaries
dicts = {'key1': 1, 'key2': 2, 'key3': 3}

for item in dicts.items():
    print(item)

# get all value Using tuple unpacking technique.
for key, value in dicts.items():
    print(value)

# Nested for loop
my_list1 = []
for x in [2, 3, 4]:
    for y in [100, 200, 300]:
        my_list1.append(x * y)
print(my_list1)
# ************** While Loop **************

count = 0
while count < 10:
    count += 1
    print(count)
