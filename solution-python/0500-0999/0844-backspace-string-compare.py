class Solution(object):
    def backspaceCompare(self, S, T):
        def build(N):
            n = []
            for i in N:
                if i != "#":
                    n.append(i)
                elif n:
                    n.pop()     
            return ''.join(n)
        return build(S) == build(T)