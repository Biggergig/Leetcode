from itertools import accumulate
class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        ans = 0
        for i in range(len(heights)):
            ans = max(
                ans,
                sum(accumulate(heights[i::-1], min)) \
                + sum(accumulate(heights[i:], min)) \
                - heights[i]
            )
        return ans