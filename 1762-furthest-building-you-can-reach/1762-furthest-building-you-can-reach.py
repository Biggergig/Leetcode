from heapq import *
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        deltas = [max(b-a,0) for a,b in zip(heights,heights[1:])]
        used_lad = []
        for i,d in enumerate(deltas):
            if d == 0: continue
            heappush(used_lad,d)
            if len(used_lad) > ladders:
                need_bricks = heappop(used_lad)
                if bricks < need_bricks:
                    return i
                bricks -= need_bricks
        return len(heights)-1