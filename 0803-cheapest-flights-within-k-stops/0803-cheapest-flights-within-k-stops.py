from heapq import *
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i:{} for i in range(n)}
        for a,b,cost in flights:
            adj[a][b] = cost
        Q = [(0, -1, src)]
        seen = set()
        while Q:
            cost, stops, pos = heappop(Q)
            if pos == dst: return cost
            if stops == k: continue

            if (stops,pos) in seen: continue
            seen.add((stops,pos))

            for e,c in adj[pos].items():
                if (stops+1, e) in seen: continue
                heappush(Q, (cost + c, stops+1, e))
                
        return -1