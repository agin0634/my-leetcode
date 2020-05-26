class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = 0
        for i in s:
            if count == len(t): return False
            while t[count] != i:
                count += 1
                if count == len(t):
                    return False
            count += 1
        return True