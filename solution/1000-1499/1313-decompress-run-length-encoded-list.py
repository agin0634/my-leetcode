class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        
        for i in range(len(nums)/2):
            res.extend([nums[2*i+1]] * nums[2*i])
        return res
        