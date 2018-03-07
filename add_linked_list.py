# Definition for singly-linked list.
import json

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        lst_num1 = self.link_to_list(l1)
        lst_num2 = self.link_to_list(l2)
        lst_sum = []

        while len(lst_num1) > 0 and len(lst_num2) > 0:
            num1 = lst_num1.pop(0)
            num2 = lst_num2.pop(0)
            lst_sum.append(num1 + num2)
        if len(lst_num1) == 0 and len(lst_num2) > 0:
            lst_sum = lst_sum + lst_num2
        elif len(lst_num2) == 0 and len(lst_num1) > 0:
            lst_sum = lst_sum + lst_num1

        for index in range(len(lst_sum) - 1):
            num = lst_sum[index]
            if num >= 10:
                lst_sum[index] = lst_sum[index] - 10
                lst_sum[index + 1] = lst_sum[index + 1] + 1

        if lst_sum[-1] >= 10:
            lst_sum[-1] = lst_sum[-1] - 10
            lst_sum.append(1)

        sumLink = ListNode(lst_sum[0])
        sumNode = sumLink
        for index in range(1, len(lst_sum)):
            num = lst_sum[index]
            newNode = ListNode(num)
            sumNode.next = newNode
            sumNode = sumNode.next

        return sumLink

    def link_to_list(self, l):
        lst_num = []
        lst_num.append(l.val)
        while l.next:
            l = l.next
            lst_num.append(l.val)
        return lst_num



def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            l1 = stringToListNode(line)
            line = lines.next()
            l2 = stringToListNode(line)

            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()