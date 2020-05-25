# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = []
        temp = head
        res = curr = ListNode(0)
        while temp:
            s.append(temp.val)
            temp = temp.next
        s = sorted(s)
        
        for i in s:
            curr.next = ListNode(i)
            curr = curr.next
        return res.next