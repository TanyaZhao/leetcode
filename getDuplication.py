# coding:utf-8
# 不修改数组，找出重复的数字
def getDuplication(nums, length):
    if nums is None or length <= 0:
        return -1

    start = 1
    end = length - 1
    while start <= end:
        middle = (end - start)/2 + start
        # 统计start到middle中数字出现的次数
        count = countRange(nums, length, start ,middle)
        if end == start:
            if count > 1:
                return start
            else:
                break

        if count > middle-start+1:
            end = middle
        else:
            start = middle + 1

    return -1


def countRange(nums, length, start, end):
    '''
    统计start到end中数字出现的次数
    :param nums:
    :param start:
    :param end:
    :return:
    '''
    if nums is None:                                                                                                                                                        
        return 0

    count = 0
    for i in range(length):
        if nums[i] >= start and nums[i] <= end:
            count = count + 1

    return count


print(getDuplication([2,3,5,4,3,2,6,7], 8))