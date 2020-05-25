# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = curr = ListNode(0)
        while head and head.next:
            curr.next = ListNode(head.next.val)
            curr.next.next = ListNode(head.val)
            curr = curr.next.next
            head = head.next.next
        
        if head:
            curr.next = ListNode(head.val)
        
        return res.next