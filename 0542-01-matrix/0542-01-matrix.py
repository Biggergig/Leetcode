from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        for y in range(len(mat)):
            for x in range(len(mat[0])):
                if mat[y][x] == 0:
                    q.appendleft((x,y,0))
                mat[y][x]=inf
        while q:
            x,y,d = q.pop()
            if not (0<=x<len(mat[0]) and 0<=y<len(mat)): continue
            if mat[y][x] <= d: continue
            mat[y][x] = d
            for dx in (-1, 1):
                q.appendleft((x+dx,y,d+1))
                q.appendleft((x,y+dx,d+1))
        return mat