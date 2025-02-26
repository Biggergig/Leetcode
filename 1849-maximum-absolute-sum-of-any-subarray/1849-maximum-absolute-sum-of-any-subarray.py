class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curPos=curNeg=0
        best=nums[0]
        for n in nums:
            curPos = max(curPos+n, n)
            curNeg = min(curNeg+n, n)
            best=max(best,abs(curPos),abs(curNeg))
        return best