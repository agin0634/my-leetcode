class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        a = collections.Counter(A.split())
        b = collections.Counter(B.split())
        c = a+b
        
        return [k for k,v in c.items() if v == 1]
            