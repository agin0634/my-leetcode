class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        dict = {}
        stack = []
        res = []
        
        for i in nums2:
            
            while stack and i > stack[-1]:
                dict[stack.pop()] = i
            
            stack.append(i)
            
        for x in nums1:
            if x in dict:
                res.append(dict[x])
            else:
                res.append(-1)
        
        return res
            