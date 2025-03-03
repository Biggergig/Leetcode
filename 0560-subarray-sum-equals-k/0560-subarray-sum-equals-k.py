from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumsum = 0
        seen_sums = defaultdict(int, {0:1})
        ans = 0
        for v in nums:
            cumsum += v
            ans += seen_sums.get(cumsum-k,0)
            seen_sums[cumsum]+=1
        return ans