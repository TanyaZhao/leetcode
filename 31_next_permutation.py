# coding:utf-8
# 1. 先从后往前定位第一个逆序的下标
# 2. 在从后往前定位第一个比这个逆序大的数
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        def partition(arr, low, high):
            i = (low - 1)  # 最小元素索引
            pivot = arr[high]

            for j in range(low, high):

                # 当前元素小于或等于 pivot
                if arr[j] <= pivot:
                    i = i + 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return (i + 1)

        def quickSort(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)

                quickSort(arr, low, pi - 1)
                quickSort(arr, pi + 1, high)

        is_finished = False

        if len(nums) > 1:
            # for start in range(len(nums) - 1, -1, -1):
            #     if not is_finished:
            #         for end in range(start - 1, -1, -1):
            #             if nums[end] < nums[start]:
            #                 temp = nums[end]
            #                 nums[end] = nums[start]
            #                 nums[start] = temp
            #                 quickSort(nums, end + 1, len(nums) - 1)
            #                 is_finished = True

            i = len(nums) - 2
            j = len(nums) - 1

            while(i>=0 and nums[i] >= nums[i+1]):
                i -= 1

            while (j >= 0 and nums[j] <= nums[i]):
                j -= 1
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            quickSort(nums, i + 1, len(nums) - 1)


solution = Solution()
nums = [4,2,0,2,3,2,0]
solution.nextPermutation(nums)
print(nums)