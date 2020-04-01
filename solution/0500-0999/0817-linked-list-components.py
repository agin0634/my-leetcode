# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        G =  set(G)
        curr = head
        count = 0
        while curr:
            if curr.val in G:
                count += 1
                while curr and curr.val in G:
                    curr = curr.next
            else:
                curr = curr.next
        return count