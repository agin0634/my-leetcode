class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = ""
        for c in str:
            if ord(c) <= 90 and ord(c) >= 65:
                res += chr(ord(c) + 32)
            else:
                res += c
        return res