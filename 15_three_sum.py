class Solution(object):
    def threeSum(self, num):
        num.sort()
        res = []
        for i in range(len(num) - 2):
            if i == 0 or num[i] > num[i - 1]:
                left = i + 1;
                right = len(num) - 1
                while left < right:
                    if num[left] + num[right] == -num[i]:
                        res.append([num[i], num[left], num[right]])
                        left += 1;
                        right -= 1
                        while left < right and num[left] == num[left - 1]: left += 1
                        while left < right and num[right] == num[right + 1]: right -= 1
                    elif num[left] + num[right] < -num[i]:  # need to increase num[left] + num[right]
                        while left < right:
                            left += 1
                            if num[left] > num[left - 1]: break # to discard the case that num[left] = num[left-1]
                    elif num[left] + num[right] > -num[i]:  # need to decrease num[left] + num[right]
                        while left < right:
                            right -= 1
                            if num[right] < num[right + 1]: break # to discard the case that num[right] = num[right+1]
        return res


solution = Solution()
ret = solution.threeSum([-1, 0, 1, 2, -1, -4])
print(ret)