# Created by vidit.singh at 03-03-2022

def get_sum(a, b):
    return sum((a, b)) * 0.5


print(get_sum(100, 200))


# to pass multiple arguments
def get_multiple_args(*args):
    print(args)  # Return tuples of arguments
    return sum(args)


print(get_multiple_args(1, 2, 3, 4, 5))


# keyword args kwargs takes input as dictionary.
def get_kwargs(**kwargs):
    print(kwargs)
    print(f"Hi my choice is {kwargs['game2']}")


print(get_kwargs(game='cricket', game2='hockey'))


def mix_args(*args, **kwargs):
    print(args)
    print(kwargs)
    print(f"Hi, Thi is example of args {args[2]}, and kwargs {kwargs['fname']}")


print(mix_args('Hi', 'Hello', 'World', fname='vidit', lname='Singh'))
