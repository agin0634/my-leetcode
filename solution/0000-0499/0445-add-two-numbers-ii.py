# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        L1, L2 = [], []
        sum = 0
        prev = None
        while l1:
            L1.append(l1.val)
            l1 = l1.next
        while l2:
            L2.append(l2.val)
            l2 = l2.next
        while L1 or L2 or sum:
            if L1:
                sum += L1.pop()
            if L2:
                sum += L2.pop()
            curr = ListNode(sum%10)
            sum //= 10
            curr.next = prev
            prev = curr
        return prev