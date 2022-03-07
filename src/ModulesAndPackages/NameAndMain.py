# Created by vidit.singh at 04-03-2022

# __name__ is a built-in variable which is assigned to __main__ if he files is run/called itself, if the file is
# imported to other python script then __name__ value becomes name of the class not __main__.

def add(n1, n2):
    return n1 + n2


print(__name__)
# We can organise def calls inside if block so that it is called only through main. It will not call those method in
# imports implicitly.
if __name__ == '__main__':
    print(add(2, 3))
