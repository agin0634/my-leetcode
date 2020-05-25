class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        sum = 0
        
        for i in ops:
            if i.lstrip('-').isdigit():
                sum += int(i)
                stack.append(int(i))
            elif i == "C":
                popped = stack.pop()
                sum -= popped
            elif i == "D":
                popped = stack[-1]
                popped *= 2
                sum += popped
                stack.append(popped)
            elif i == "+":
                popped = stack[-1] + stack[-2]
                sum += popped
                stack.append(popped)
        return sum