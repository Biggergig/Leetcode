from heapq import *
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        used_lad = []
        for i in range(len(heights)-1):
            d = heights[i+1]-heights[i]
            if d <= 0: continue
            heappush(used_lad,d)
            if len(used_lad) > ladders:
                need_bricks = heappop(used_lad)
                if bricks < need_bricks:
                    return i
                bricks -= need_bricks
        return len(heights)-1