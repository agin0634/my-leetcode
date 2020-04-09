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
                prev = None
                while stemp:
                    curr = stemp
                    stemp = stemp.next
                    curr.next = prev
                    prev = curr
                while prev:
                    r.next = ListNode(prev.val)
                    prev = prev.next
                    r = r.next
            head = head.next
            
        if count > 0:
            while temp.next:
                r.next = ListNode(temp.next.val)
                temp = temp.next
                r = r.next
                
        return res.next