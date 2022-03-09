# Created by vidit.singh at 08-03-2022
"""Python provides a generator to create your own iterator function. A generator is a special type of function which
does not return a single value, instead, it returns an iterator object with a sequence of values. In a generator
function, a yield statement is used rather than a return statement. """


def square_of_sequence(x):
    for i in range(x):
        yield i * i


op = square_of_sequence(5)
for p in op:
    print(f"hi {p}")

# Would throw 'StopIteration' because 'op' generator object has already iterated using for loop.
# print(f"op{next(op)}")

# To print again call generator function again
op1 = square_of_sequence(5)
while True:
    try:
        print(f"Hello {next(op1)}")
    except StopIteration:
        break

# Strings can also be converted to iterators

s = 'Vidit'
for k in s:
    print(k)

s_itr = iter(s)
print(next(s_itr))
print(next(s_itr))

my_list = [1, 2, 3, 4, 5]

# generators help to eliminate use of storing data in memory.
my_gen = (item for item in my_list if item > 2)

for it in my_gen:
    print(it)
