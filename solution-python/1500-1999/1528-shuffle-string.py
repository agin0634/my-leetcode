class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res = [0]*len(indices)
        for i in range(len(s)):
            res[indices[i]] = s[i]
        return ''.join(res)