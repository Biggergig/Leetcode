class Solution:
    def coloredCells(self, n: int) -> int:
        ans = 1
        for t in range(1,n):
            ans += 4*t
        return ans

    def coloredCells(self, n: int) -> int:
        return 1 + 4*sum(range(1,n))

    def coloredCells(self, n: int) -> int:
        return 1 + 4*((n-1)*n)//2