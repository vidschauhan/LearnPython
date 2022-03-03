# Created by vidit.singh at 03-03-2022

"""
LESSER OF TWO EVENS :  Write a function that returns the lesser of two given numbers if both the numbers are even,
but returns the greater if one or both numbers are odd.
"""


def lesser_of_two_evens(*args):
    num = -1
    for item in args:
        if item % 2 == 0:
            if args[0] > args[1]:
                num = args[1]
            else:
                num = args[0]
        else:
            if args[0] > args[1]:
                num = args[0]
            else:
                num = args[1]
    return num


print(lesser_of_two_evens(2, 5))
