class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict = {}
        res = []
        for i in nums1:
            if i not in dict:
                dict[i] = 0
            
        for j in nums2:
            if j in dict:
                dict[j] += 1
                
        for k,i in dict.items():
            if i > 0:
                res.append(k)       
        return res