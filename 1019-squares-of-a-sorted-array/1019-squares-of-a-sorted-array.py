from bisect import *
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = min(bisect_left(nums,0), len(nums)-1)
        while l>=0 and nums[l] > 0:
            l-=1
        r = l+1
        out = []
        while 0<=l or r<len(nums):
            L = abs(nums[l]) if l>=0 else inf
            R = abs(nums[r]) if r<len(nums) else inf
            if L < R:
                out.append(L**2)
                l-=1
            else:
                out.append(R**2)
                r+=1
        return out