class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min, temp = 0, 0
        for i in nums:
            temp += i
            if temp < min:
                min = temp
        return -min+1