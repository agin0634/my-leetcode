class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if '00' in bin(n) or '11' in bin(n) else True
    