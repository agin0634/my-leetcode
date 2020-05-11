class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        for i in s:
            dict[i] = dict.get(i, 0)+1
        for i, e in enumerate(s):
            if dict[e] == 1:
                return i
        return -1