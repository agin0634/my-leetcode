class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        dict, res= {}, 0
        for c in chars:
            if c not in dict:
                dict[c] = 1
            else:
                dict[c] += 1
        for w in words:
            copy = dict.copy()
            Formed = True
            for c in w:
                if c not in copy or copy[c] == 0:
                    Formed = False
                    break
                else:
                    copy[c] -= 1
            if Formed:
                res += len(w)
        return res