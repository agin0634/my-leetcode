class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        A = list(range(len(S)+1))
        res = []
        for s in range(len(S)):
            if S[s] == "I":
                res.append(A.pop(0))
            else:
                res.append(A.pop())
        return res + A