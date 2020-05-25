class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        res = []
        words = text.split()
        for i in range(len(words)-2):
            if words[i] == first:
                if words[i+1] == second:
                    res.append(words[i+2])
        return res