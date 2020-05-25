class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        que = collections.deque()
        deck = sorted(deck)
        while deck:
            if que:
                que.appendleft(que.pop())
            que.appendleft(deck.pop())
        return list(que)