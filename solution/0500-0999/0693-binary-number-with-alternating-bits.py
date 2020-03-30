class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        curr = 2
        for i in bin(n)[2:]:
            if i != curr:
                curr = i
            else:
                return False
        return True