# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        res = []
        if head.next == None:
            return int(str(head.val),2)
        
        while head:
            res.append(str(head.val))
            head = head.next
        return int("".join(res),2)