class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur=best=-inf
        for n in nums:
            cur = max(cur+n,n)
            best=max(best,cur)
        return best