# Created by vidit.singh at 02-03-2022
"""
 @ Selection sot using Python.
"""


def selection_sort(unsorted_list):
    for index in range(len(unsorted_list)):
        minimum = index
        for j in range(index + 1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[minimum]:
                minimum = j

        temp = unsorted_list[index]
        unsorted_list[index] = unsorted_list[minimum]
        unsorted_list[minimum] = temp

    return unsorted_list


sorted_list = selection_sort([3, 17, 11, 5, 7, 6])
print(sorted_list)
