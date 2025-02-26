class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best,cur=float('-inf'),0
        for n in nums:
            cur=max(n,cur+n)
            best=max(best,cur)
        return best