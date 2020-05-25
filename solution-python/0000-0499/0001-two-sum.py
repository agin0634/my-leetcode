class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        
        for i,e in enumerate (nums):
            other = target - e
            
            if other in seen:
                return [seen[other], i]
            else:
                seen[e] = i