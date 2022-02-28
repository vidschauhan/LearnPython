# Created by vidit.singh at 28-02-2022

# Assesment

# Q1. Use for, Split() and if to create a statement that will print out words starts with 's'.
s1 = 'print out words starts with s'
list_str = s1.split()
# print(list_str)
for item in list_str:
    if item.startswith('s'):
        pass
        # print(item)

# Q2. List comprehension to create a list of all numbers between 1 and 50 div by 3.

list_div_3 = [temp for temp in range(1, 50) if temp % 3 == 0]
# print(list_div_3)

# Q3. Go through the string below and if the length of a word is even print 'even'.
str1 = 'Print every word in this sentence that has an even number of letters'
list_even = str1.split()

lis = ['Even' for it in list_even if len(it) % 2 == 0]
print(lis)

count = 0
for idx, ch in enumerate(list_even):
    if len(ch) % 2 == 0:
        print(f'index : {idx}, word : {ch}, length : {len(ch)}, Even')
        count += 1
print(f'Total words : {count}')

# Q4. Print 1 to 100. But if multiple of 3 'Fizz', Multiple of 5 'Buzz' & But Multiple of both 3 & 5 'FizzBuzz'.

for item in range(1, 101):
    if item % 3 == 0 and item % 5 == 0:
        print('FizzBuzz')
    elif item % 5 == 0:
        print('Buzz')
    elif item % 3 == 0:
        print('Fizz')
    else:
        print(item)

# Q5. Use list comprehension to create alist of the first letters of every word in the string.
ss = "Create a list of the first letters of every word in this string"
final_list = [it[0] for it in ss.split()]
print(final_list)
