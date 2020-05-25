# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        res = prev = ListNode(0)
        temp = None
        count = 1
        while head:
            curr = head
            if count == m:
                while head:
                    curr = head
                    head = head.next
                    count += 1
                    curr.next = temp
                    temp = curr
                    if count > n:
                        break
                prev.next = temp
                while prev.next:
                    prev = prev.next
            else:
                head = head.next
                count += 1
                prev.next =curr
                prev = prev.next      
        return res.next