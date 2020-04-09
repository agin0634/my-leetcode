# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        curr, size = head, 1
        while curr.next:
            size += 1
            curr = curr.next
        r = size - (k%size)
        curr.next = head
        for i in range(r):
            curr = curr.next
        res = curr.next
        curr.next = None
        return res