# Created by vidit.singh at 04-03-2022

def insertion_sort(sort_list):
    for i in range(1, len(sort_list)):
        # curr_element variable contains the data we intend on bringing over to  the  sorted area.
        curr_element = sort_list[i]
        j = i - 1
        while j >= 0 and sort_list[j] > curr_element:
            sort_list[j + 1] = sort_list[j]  # Overwrite the j+1 pos with jth element until you reach to sorted area
            j -= 1

        sort_list[j + 1] = curr_element  # Insert the intended element to j + 1 th position.
    return sort_list


print(insertion_sort([7, 34, 6, 32, 87, 3, 11]))
