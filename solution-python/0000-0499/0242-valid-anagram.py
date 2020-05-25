class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        dictS, dictT = {}, {}
        for c in s: 
            dictS[c] = dictS.get(c, 0) + 1
        for c in t:
            dictT[c] = dictT.get(c, 0) + 1
        for k, v in dictS.items():
            if k not in dictT or dictT[k] != v:
                return False
        return True