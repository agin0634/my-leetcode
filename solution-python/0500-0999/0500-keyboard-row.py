class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        roa, res = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')], []
        for w in words:
            word = set(w.lower())
            for i in roa:
                if word.issubset(i):
                    res.append(w)
        return res