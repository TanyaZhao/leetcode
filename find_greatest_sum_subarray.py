def find_greatest_sum_of_subarray(array):
    cur_sum_list = []
    max_sum_util_now_list = []
    max_sub_string_start = 0
    i = 0

    cur_sum = 0
    max_sum_util_now = 0
    while i < len(array):
        cur_num = array[i]
        cur_sum += cur_num

        if cur_sum < cur_num:
            max_sub_string_start = i
            cur_sum = cur_num
            max_sum_util_now = cur_sum
        elif max_sum_util_now < cur_sum:
            max_sum_util_now = cur_sum

        cur_sum_list.append(cur_sum)
        max_sum_util_now_list.append(max_sum_util_now)
        i += 1

    max_sub_string_end = cur_sum_list.index(max_sum_util_now)

    print(max_sum_util_now)
    print(max_sum_util_now_list)
    print(cur_sum_list)
    print([array[i] for i in range(max_sub_string_start, max_sub_string_end+1)])


def find_greatest_sum_of_subarray_dynamic(array):
    cur_sum_list = []
    max_sum_util_now_list = []
    max_sub_string_start = 0
    i = 0

    pre_max_sum = 0
    max_substring = 0
    while i < len(array):
        cur_num = array[i]
        # cur_sum += cur_num

        if pre_max_sum <= 0:
            cur_max_sum = cur_num
            max_sub_string_start = i
        elif pre_max_sum > 0:
            cur_max_sum = pre_max_sum + cur_num
        max_substring = cur_max_sum if cur_max_sum > pre_max_sum else pre_max_sum

        cur_sum_list.append(cur_max_sum)
        max_sum_util_now_list.append(max_substring)
        pre_max_sum = cur_max_sum
        i += 1

    max_sub_string_end = max_sum_util_now_list.index(max_substring)

    print(max_substring)
    print(max_sum_util_now_list)
    print(cur_sum_list)
    print([array[i] for i in range(max_sub_string_start, max_sub_string_end + 1)])


find_greatest_sum_of_subarray([1, -2, 3, 10, -4, 7, 2, 0, 0, -1])
print()
find_greatest_sum_of_subarray_dynamic([1, -2, 3, 10, -4, 7, 2, 0, 0, -1])
