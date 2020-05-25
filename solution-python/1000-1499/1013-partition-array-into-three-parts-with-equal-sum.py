class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        target =  sum(A)/3
        temp,part = 0,0
        for a in A:
            temp += a
            if temp == target:
                temp = 0
                part += 1
        if part >= 3:
            return True
        else:
            return False
                