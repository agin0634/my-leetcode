# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        temp = t = ListNode(0)
        res = r = ListNode(0)
        count = 0
        while head:
            t.next = ListNode(head.val)
            t = t.next
            count += 1
            if count == k:
                stemp = temp.next
                temp = t
                count = 0
                prev = self.reverse(stemp)
                while prev:
                    r.next = ListNode(prev.val)
                    prev = prev.next
                    r = r.next
            head = head.next
        if count > 0:
            r.next = temp.next
        return res.next
    
    def reverse(self, h):
        prev = None
        while h:
                curr = h
                h = h.next
                curr.next = prev
                prev = curr
        return prev