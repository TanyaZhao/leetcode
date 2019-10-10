class Solution(object):
    def isValid_dummy(self, s):
        """
        :type s: str
        :rtype: bool
        """

        help_dict = {"(":-1, ")":1, "[":-2, "]":2, "{":-3, "}":3}

        if len(s) == 0:
            return True

        if len(s) % 2 == 0:
            flag = [-1] * len(s)

            i = 0
            j = len(s) -1

            while i < j:
                if flag[i] == -1:
                    if flag[j] == -1:
                        if (help_dict[s[i]] + help_dict[s[j]] != 0):
                            j -= 1
                        else:
                            if (j-i) % 2 == 1:
                                flag[i] = 0
                                flag[j] = 0
                                j = len(s) -1
                                i += 1
                                continue
                            elif (j-i) % 2 == 0:
                                j -= 1
                    else:
                        j -= 1
                else:
                    i += 1


            if sum(flag) == 0:
                return True
            else:
                return False

        else:
            return False

    def isValid_stack(self, s):

        stack = []

        # ([{ : open bracket
        # )]} : close bracket
        mapping = {")":"(", "]":"[", "}":"{"}

        for str in s:
            if str in mapping:  # if str is close bracket
                top_ele = stack.pop() if stack else "#"
                if top_ele != mapping[str]:
                    return False
            else:
                stack.append(str)

        if stack:
            return False
        else:
            return True



solution = Solution()
print(solution.isValid_stack("}"))




