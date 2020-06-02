class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        if nums[-1] != len(nums):
            return len(nums)
        elif nums[0] != 0:
            return 0
        for i in range(1,len(nums)):
            n = nums[i-1]+1
            if nums[i] != n:
                return n