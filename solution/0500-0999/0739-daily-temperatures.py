class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        dict, stack, res, currDay= {}, [], [0]*len(T), 0
        for t in T:
            dict[currDay] = t
            while stack:
                if t > dict[stack[-1]]:
                    pop = stack.pop()
                    res[pop] = currDay - pop
                else:
                    break
            stack.append(currDay)
            currDay += 1
        return res