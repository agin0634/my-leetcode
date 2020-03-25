class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(26,0,-1):
            if i < 10:
                s = s.replace(str(i),chr(96+i))
            else:
                s = s.replace(str(i)+"#",chr(96+i))
        return s