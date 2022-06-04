# Created by vidit.singh at 14-05-2022

import array as arr

int_type_array = arr.array('i', [1, 2, 3, 4, 5])


def print_data(array1):
    for item in array1:
        print(item, end=' ')
    print('\n')


print_data(int_type_array)

int_type_array.insert(1, 444)  # Insert at first position of the array.
print_data(int_type_array)
