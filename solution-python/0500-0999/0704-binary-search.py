class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, up = 0, len(nums)-1
        mid = (low+up)/2
        while up >= low:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid+1
            else:
                up = mid-1
            mid = (low+up)/2
        return -1