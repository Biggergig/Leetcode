class Solution:
    def DFS(self, x, y):
        if not (0<=x<len(self.grid[0]) and 0<=y<len(self.grid)): return 0
        if self.grid[y][x] != '1': return 0
        self.grid[y][x] = '0'
        self.DFS(x+1,y)
        self.DFS(x-1,y)
        self.DFS(x,y+1)
        self.DFS(x,y-1)
        return 1
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        ans = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                ans += self.DFS(x,y)

        return ans
    
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        def mark(x,y):
            if not (0<=x<len(grid[0]) and 0<=y<len(grid)) or grid[y][x] == '0': return
            grid[y][x] = '0'
            mark(x-1,y)
            mark(x+1,y)
            mark(x,y-1)
            mark(x,y+1)
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '1':
                    ans+=1
                    mark(x,y)
        return ans