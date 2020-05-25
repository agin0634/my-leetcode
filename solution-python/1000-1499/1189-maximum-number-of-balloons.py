class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        cob = {'b':1, 'a':1, 'l':2, 'o':2, 'n':1}
        dict = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
        for c in text:
            if c in dict:
                dict[c] += 1
        res = []
        for k, v in cob.items():
            res.append(dict[k]/v)
        return min(res)