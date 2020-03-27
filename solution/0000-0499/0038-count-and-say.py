class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        base = "1"
        i = 1
        while i < n:
            stack= []
            temp = ""
            for c in base:
                if stack and c != stack[-1]:
                    temp += str(len(stack))+stack.pop()
                    stack *= 0
                    stack.append(c)
                else:
                    stack.append(c)
            temp += str(len(stack))+stack.pop()
            base = temp
            i += 1
        return base