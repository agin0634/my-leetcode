class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        res = ""
        flag = False
        for s in str(num):
            if s == "6" and not flag:
                s = "9"
                flag = True
            res += s
        return int(res)
            