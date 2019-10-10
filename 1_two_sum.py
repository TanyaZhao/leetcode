def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # target_list = []
    # dict_num = {}
    # for index, num in enumerate(nums):
    #     dict_num[num] = index
    #
    # for num, index in dict_num.items():
    #     diff = target - num
    #     if dict_num.has_key(diff):
    #         index2 = dict_num[diff]
    #         target_list.append(index)
    #         target_list.append(dict_num[diff])
    #         target_list.sort()
    #         return target_list
    #     else:
    #         continue
    dict = {}
    for i in range(len(nums)):
        x = nums[i]
        if target - x in dict:
            return [dict[target - x], i]
        dict[x] = i


print(twoSum([3,5,3], 6))