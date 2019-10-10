# # coding:utf-8
# # 剑指offer P197: 输入一个字符串，打印字符串中的字符能组成的所有排列
#
# def get_all_permutation(str):
#     all_permutation = [str]
#     all_permutation.append(permutation(str))
#
#     return all_permutation
#
# # def permutation(str, sub_str):
# #     if len(sub_str) == 0:
# #         print(str)
# #
# #     else:
# #         for i in range(1,len(str)):
# #             cur_str = swap(str, 0, i)
# #             # all_permutation.append(cur_str)
# #             permutation(cur_str[0:i], cur_str[i:])
# #             cur_str = swap(str, 0, i)
#
# def permutation(s=''):
#     if len(s) <= 1:
#         return [s]
#     sl = []
#     for i in range(len(s)):
#         for j in permutation(s[0:i] + s[i + 1:]):
#             sl.append(s[i] + j)
#     return sl
#
#
# def swap(array, index1, index2):
#     array = list(array)
#     array[index1], array[index2] = array[index2], array[index1]
#     return "".join(array)
#
#
# all_per = get_all_permutation("abc")

def perm(s=''):
    if len(s) <= 1:
        return [s]
    sl = []
    for i in range(len(s)):
        for j in perm(s[0:i] + s[i + 1:]):
            sl.append(s[i] + j)
    return sl


def main():
    # 可能包含重复的串
    perm_nums = perm('abc')
    # 对结果去重
    no_repeat_nums = list(set(perm_nums))
    print('perm_nums', len(perm_nums), perm_nums)
    print('no_repeat_nums', len(no_repeat_nums), no_repeat_nums)
    pass


if __name__ == '__main__':
    main()
