class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = []
        S = S.split()
        count = 1
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        for s in S:
            if s[0] not in vowel:
                s = s[1:] + s[0]     
            s += 'ma' + 'a' * count
            count+=1
            res.append(s)
        return " ".join(res)
            
            