class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0]*n for _ in range(n)]
        self.n=n
        

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        for i in range(self.n):
            if set(self.board[i]) == {player}: return player
            if set([row[i] for row in self.board]) == {player}: return player
        if set([row[y] for y,row in enumerate(self.board)]) == {player}: return player
        if set([row[-y-1] for y,row in enumerate(self.board)]) == {player}: return player
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)