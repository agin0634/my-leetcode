class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        for a in A:
            if a % 2 == 0:
                res.insert(0, a)
            else:
                res.append(a)
        return res