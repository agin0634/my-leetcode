class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, nums = [], []
        curr = ""
        num = ""
        
        for i in s:
            if i.isdigit():
                num += i
            elif i == "[":
                nums.append(num)
                num = ""
                stack.append(curr)
                curr = ""
            elif i == "]":
                popped = nums.pop()
                curr *= int(popped)
                if stack:   
                    curr = stack.pop() + curr
            else:
                curr += i
                
        return curr