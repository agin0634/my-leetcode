class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        res = []
        o = sum(shifts) % 26
        for i,e in enumerate(S):
            index = ord(e) - ord('a')
            res.append(chr(ord('a')+(index+o)%26))
            o = (o - shifts[i]) % 26
        return "".join(res)