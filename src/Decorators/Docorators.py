# Created by vidit.singh at 07-03-2022

# Decorators are used to add some extra functionalities in the methods. These are used as wrappers. @new_decorator
# code behind the scene

def my_new_func(dec_func1):
    def wrap_func():
        print('Prints before decorator function')
        dec_func1()
        print('Prints after decorator function')

    return wrap_func


@my_new_func
def dec_func():
    print("Hi, I am decorator function!")


# call if you didn't put @ on de_function
# op = my_new_func(dec_func)
# print(op())

# else just call
print(dec_func())
