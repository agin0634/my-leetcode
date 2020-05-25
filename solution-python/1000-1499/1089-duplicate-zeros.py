class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        L,i = len(arr),0
        while i < L:
            if arr[i] == 0:
                i += 1
                arr.pop()
                arr.insert(i,0)
            i += 1