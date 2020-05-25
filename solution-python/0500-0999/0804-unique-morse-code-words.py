class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dict = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f":"..-.", "g": "--.", "h": "...."
        , "i": "..","j": ".---", "k":"-.-", "l": ".-..", "m": "--", "n": "-.","o": "---", "p": ".--.", "q": "--.-"
        ,"r": ".-.", "s": "...", "t": "-", "u": "..-","v": "...-", "w":".--", "x": "-..-", "y": "-.--", "z": "--.."}
        res = []
        for s in words:
            temp = ""
            for c in s:
                temp += dict[c]
            if temp not in res:
                res.append(temp)
        return len(res)