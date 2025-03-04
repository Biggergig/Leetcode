class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = inf
        best = 0
        for n in prices:
            if n-mn > best:
                best=n-mn
            if n<mn:
                mn=n
        return best