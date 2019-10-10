# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # merge one by one  => time limit exceeded
    def mergeKLists_one_by_one(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        if lists:
            cur_list = lists[0]
            if len(lists) > 1:
                for i in range(1, len(lists)):
                    cur_list = self.mergeTwoLists(cur_list, lists[i])
            return cur_list
        else:
            cur_list = ListNode(0)
            return cur_list.next

    # merge by devide and conquer
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        amount = len(lists)
        interval = 1
        while amount > interval:
            for i in range(0, amount-interval, 2*interval):
                lists[i] = self.mergeTwoLists(lists[i], lists[i+interval])
            interval *= 2
        return lists[0] if amount > 0 else lists


    def creat_list(self, list):
        p_head = ListNode(None)
        p = p_head
        for i in list:
            p_node = ListNode(i)
            p.next = p_node
            p = p.next

        return p_head.next

    def print_list(self, p):
        print_list=[]
        if p:
            while p.next:
                print_list.append(str(p.val) + "->")
                p = p.next
            print_list.append(str(p.val))
            print("".join(print_list))
        else:
            print(p)

    def mergeTwoLists(self, p, q):
        head = None

        if not p:
            return q
        if not q:
            return p

        if p.val < q.val:
            head = p
            head.next = self.mergeTwoLists(p.next, q)
        else:
            head = q
            head.next = self.mergeTwoLists(p, q.next)

        return head

solution = Solution()
lists = [[1],[1],[-1],[-2],[6]]
# lists = []
lists_node = []
for l in lists:
    lists_node.append(solution.creat_list(l))

merged_list = solution.mergeKLists(lists_node)
solution.print_list(merged_list)