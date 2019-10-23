def binary_search(nums, key):
    start = 0
    end = len(nums)

    if len(nums) == 0:
        return -1, -1

    while(end > start):
        mid_index = (end+start) // 2
        mid = nums[mid_index]

        if mid > key:
            end = mid_index - 1
        elif mid < key:
            start = mid_index + 1
            # binary_search(nums[mid+1:end], key)
        else:
            return mid_index, mid
    return -1, -1


print(binary_search([1,2,3,4,4,6,8,9,14,18,20], 7))