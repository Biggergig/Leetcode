class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}
        def dfs(x,y,lb=float('-inf')):
            # solve for the longest increasing subsequence starting at this point
            if not (0<=x<len(matrix[0]) and 0<=y<len(matrix)): return 0
            if matrix[y][x] <= lb: return 0
            if (x,y) in cache: return cache[(x,y)]
            cache[(x,y)] = max(
                dfs(x-1,y,matrix[y][x])+1,
                dfs(x+1,y,matrix[y][x])+1,
                dfs(x,y-1,matrix[y][x])+1,
                dfs(x,y+1,matrix[y][x])+1,
            )
            return cache[(x,y)]
        return max(dfs(x,y) for x in range(len(matrix[0])) for y in range(len(matrix)))
                