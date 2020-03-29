class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = [0] * len(A)
        i,j = 0,1
        for a in A:
            if a % 2 == 0:
                res[i] = a
                i += 2
            else:
                res[j] = a
                j += 2
        return res
                