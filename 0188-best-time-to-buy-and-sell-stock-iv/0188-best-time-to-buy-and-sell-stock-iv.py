class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # has[k][t] = the most amount of money if I have a coin on day t and have bought k times
        # dont[k][t]= the most amount of money if I don't have a coin at day t and have sold k times
        has = [[float('-inf')]*len(prices) for _ in range(k+1)]
        dont = [[0]*len(prices) for _ in range(k+1)]
        for t,p in enumerate(prices):
            has[0][t] = 0 # no transactions so 0 money
            for j in range(1,k+1):
                # most money I can have with j transactions is what I had yesterday, or selling today
                has[j][t] = max(has[j][t-1] if t>=0 else float('-inf'), dont[j-1][t]-p)
                dont[j][t] = max(dont[j][t-1] if t>=0 else float('-inf'),has[j][t]+p)
        return dont[-1][-1]