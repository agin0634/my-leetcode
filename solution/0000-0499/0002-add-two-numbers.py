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
        ans = curr = ListNode(0)
        o = 0
        while l1 or l2 or o != 0:
            if l1 and l2:
                m = l1.val + l2.val + o
                l1 = l1.next
                l2 = l2.next
            elif l1:
                m = l1.val + o
                l1 = l1.next
            elif l2:
                m = l2.val + o
                l2 = l2.next
            else:
                m = o
            
            if m < 10:
                o = 0
                curr.next = ListNode(m)
            else:
                m %= 10
                o = 1
                curr.next = ListNode(m)
            curr = curr.next
        return ans.next