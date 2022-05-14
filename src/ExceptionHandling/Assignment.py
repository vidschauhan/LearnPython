# Created by vidit.singh at 07-03-2022


def square_it():
    while True:
        try:
            num = int(input(" Enter a number :"))
            result = num ** 2
        except ValueError as v:
            print(f"Invalid input : {v}")
            continue
        else:
            return result


print(square_it())
