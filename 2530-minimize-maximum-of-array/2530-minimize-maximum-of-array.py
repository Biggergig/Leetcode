from heapq import *
class Solution:
    # TLE
    def minimizeArrayValue(self, nums: List[int]) -> int:
        smalls = [nums[0]]
        best = nums[0]
        for n in nums[1:]:
            if n<best:
                heappush(smalls, n)
                best = max(best, n)
            else:
                while n>smalls[0]:
                    sm = heappop(smalls)
                    move_amnt = max(best - sm, 1)
                    heappush(smalls,sm+move_amnt)
                    best = max(best, sm+move_amnt)
                    n-=move_amnt
                heappush(smalls, n)
                best = max(best, n)
        return best

    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefix_sum = 0
        ans = 0
        for i,n in enumerate(nums):
            prefix_sum+=n
            ans = max(ans,prefix_sum / (i+1))
        return math.ceil(ans)