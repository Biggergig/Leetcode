from collections import defaultdict
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[0]*3 for _ in range(3)]
        i = 1
        for x,y in moves:
            board[y][x] = i
            i*=-1
        
        for player in (1,-1):
            diags = [0,0]
            for i in range(3):
                s = [0,0]
                for j in range(3):
                    s[0]+=board[i][j]
                    s[1]+=board[j][i]
                diags[0]+=board[i][i]
                diags[1]+=board[i][-1-i]
                if player*3 in s+diags:
                    return [None,"A","B"][player] # cheeky -1 index lol
        print(*board,sep='\n')

        if len(moves) == 9: return "Draw"
        return "Pending"