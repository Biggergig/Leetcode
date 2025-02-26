from functools import cache
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @cache
        def dfs(x, y, k):
            if not(0<=x<n and 0<=y<n):return 0.
            if k == 0: return 1. # out of moves and above check failed
            return sum(
                dfs(x+dx,y+dy,k-1) for dx,dy in [
                    (-1,2),
                    (-1,-2),
                    (-2,1),
                    (-2,-1),
                    ( 1,2),
                    ( 1,-2),
                    ( 2,1),
                    ( 2,-1),
                ])/8
        return dfs(column, row, k)

