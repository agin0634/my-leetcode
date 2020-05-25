# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        res = r = ListNode(0)
        while head:
            if head.val != val:
                r.next = ListNode(head.val)
                r = r.next
            head = head.next
        return res.next