class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0: return False
        n = bin(num).replace('0b','')
        if n.count('1') == 1 and n.count('0') % 2 == 0:
            return True
        return False