# coding:utf-8
# 剑指offer P236：最长不含重复字符的子字符串

def longest_substr_without_dup(str):
    previous_position = {}

    cur_max_len = 0
    cur_max_sub_str = ""
    for i in range(len(str)):
        if str[i] in previous_position: # 之前出现过
            if(i - previous_position[str[i]]) > cur_max_len:
                cur_max_len += 1
                cur_max_sub_str = cur_max_sub_str + str[i]
            else:# str[i]在候选子串中
                cur_max_len = i - previous_position[str[i]]
                cur_max_sub_str = str[previous_position[str[i]]+1:i] + str[i]
        else:
            cur_max_len += 1
            cur_max_sub_str = cur_max_sub_str + str[i]

        previous_position[str[i]] = i

    print(cur_max_len)
    print(cur_max_sub_str)


max_sub_str_len = longest_substr_without_dup("arabcarslcgvmqcfr")

