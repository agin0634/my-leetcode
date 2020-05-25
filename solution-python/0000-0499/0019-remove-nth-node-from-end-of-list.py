# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp, size = head, 0
        while temp:
            size += 1
            temp = temp.next
        l = size - n
        
        if l == 0:
            return head.next
        
        res = head
        for i in range(1,l):
            head = head.next
        head.next = head.next.next
        return res