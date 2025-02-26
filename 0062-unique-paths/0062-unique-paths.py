class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m<n:n,m=m,n # n is smaller
        DP = [1]*n
        for _ in range(m-1):
            for i in range(1,n):
                DP[i]+=DP[i-1]
        return DP[-1]
