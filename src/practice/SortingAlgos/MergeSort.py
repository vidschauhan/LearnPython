# Created by vidit.singh at 04-03-2022


def merge_sort(input_list, start, end):
    if start <= end:
        return

    mid = (start + end) / 2
    merge_sort(input_list, 0, mid)  # for left slot list
    merge_sort(input_list, mid + 1, end)
    merge(input_list, start, mid, end)


def merge(input_list, start, mid, end):
    left_slot = start  # index on the left list
    right_slot = mid + 1  # index on the right list
    temp_list = []
    k = 0
    while left_slot <= mid and right_slot <= end:

        if input_list[left_slot] < input_list[right_slot]:
            temp_list[k] = input_list[left_slot]
            left_slot += 1
        else:
            temp_list[k] = input_list[right_slot]
            right_slot += 1
    k = + 1

    if left_slot < mid:
        while left_slot <= mid:
            temp_list[k] = input_list[left_slot]
            left_slot += 1
            k += 1
    else:
        while right_slot <= end:
            temp_list[k] = input_list[right_slot]
            right_slot += 1
            k += 1

    i = 0
    for i in range(i, len(temp_list)):
        input_list[start + i] = temp_list[i]


list1 = [45, 3, 23, 6, 75, 43, 87, 43]
merge_sort(list1, 0, len(list1) - 1)
print(list1)
