# Created by vidit.singh at 18-02-2022

# Numbers
a = 10
b = 20

print(a + b)

num1, num2, num3 = 10, 20, 30

print(num1 + (num2 % 2))

print(type(a))

# *********************** String ************************
str1 = "Hello World!"
print(str1)

print(len(str1))
a = str1[0]  # Slicing the string at 0th position.
print(a)

# String indexing and slicing
s1 = "Hi Vidit"

# To get the index of any character
print(s1[6])
print(s1[-1])  # takes index from last position.

# Slicing
print(s1[:2])  # prints Everything before first 2 character.
print(s1[2:])  # prints Everything after first 2 character.
print(s1[3:6])  # takes after 3rd index up to 6th index of string.
print(s1[3:6:7])  # takes after 3rd index up to 6th index of string.
print(s1[:: -1])  # reversing string

print(s1.upper())  # to upper case

str2 = "Hi, This is String."
print(str2.split())  # Splits white space.
print(str2.split('i'))  # Splits on i, 'i' is not present in output.

# String Formatting

print('This is a {} string.'.format('new'))  # {} act as a place holder.
print('There is {0} and {1}'.format('fox', 'goat'))  # takes input index position.
print('There is {f} and {g}'.format(f='fox', g='goat'))  # takes input index position.

result = 100 / 777
print(result)
print("output {r:1.3f}".format(r=result))  # format decimal up to 3 decimal places after decimal.

# prefer
d = 'world'
print(f'Hi,This is new {d}')  # Hi,This is new world. Formatting string using f.
