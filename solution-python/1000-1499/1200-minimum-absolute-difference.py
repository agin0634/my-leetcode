class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr = sorted(arr)
        res = []
        min = float('inf')
        for i in range(0,len(arr)-1): 
            d = abs(arr[i+1] - arr[i])
            if d < min:
                min = d
                res *= 0
                res.append([arr[i],arr[i+1]])
            elif d == min:
                min = d
                res.append([arr[i],arr[i+1]])
        return res
            