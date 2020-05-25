class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        Ry = 0
        while "R" not in board[Ry]:
            Ry+=1
        Rx = board[Ry].index("R")
        row = "".join(board[Ry][i] for i in range(8) if board[Ry][i] != ".")
        col = "".join(board[i][Rx] for i in range(8) if board[i][Rx] != ".")
        P = row + " " + col
        return P.count("Rp") + P.count("pR")