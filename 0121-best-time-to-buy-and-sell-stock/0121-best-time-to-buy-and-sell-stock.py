class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn,best = inf,0
        for n in prices:
            best = max(best,n-mn)
            mn=min(mn,n)
        return best
    
    # Faster than using max/min
    def maxProfit(self, prices: List[int]) -> int:
        mn = inf
        best = 0
        for n in prices:
            if n-mn > best:
                best=n-mn
            if n<mn:
                mn=n
        return best