class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0]*len(nums)
        for i,n in enumerate(nums):
            for j in nums:
                if n > j:
                    res[i] += 1
        return res