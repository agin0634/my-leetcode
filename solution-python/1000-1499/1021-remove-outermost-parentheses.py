class Solution(object):
    def removeOuterParentheses(self, S):
        stack = []
        res = []
        current = ""
        
        for i in S:
            current += i
            if i == "(":
                stack.append(i)
            elif i == ")":
                stack.pop()
                if not stack:
                    res.append(current[1:-1])
                    current = ""
        return "".join(res)