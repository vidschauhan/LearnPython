# Created by vidit.singh at 03-03-2022

# Map functions in Python

def square(num):
    return num ** 2


for item in map(square, [2, 3, 4, 5, 6]):
    print(item)

# or
print(list(map(square, [2, 3, 4, 5, 6])))


# Filter function

def check_even(num):
    return num % 2 == 0


for item in filter(check_even, [2, 3, 4, 5, 6]):
    print(item)


# Lambda function are anonymous function.

# Convert simple def to lambda
def square(num):
    return num ** 2


# to lambda ->>>>
var1 = lambda num: num ** 2

print(list(map(var1, [2, 3, 4, 5, 6])))
print(list(map(lambda num: num ** 2, [2, 3, 4, 5, 6])))

# passing lambda function to filter and
# converting output to list.
print(list(filter(lambda num: num % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


def range_check(num, low, high): return low <= num <= high


print(range_check(5, 4, 10))

