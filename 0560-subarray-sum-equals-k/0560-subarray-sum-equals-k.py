from collections import *
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen=Counter([0]) # track the prefix sums seen so far
        ans=s=0
        for n in nums:
            s+=n
            ans+=seen[s-k] # how many prefix sums before this can we ignore to get k
            seen[s]+=1
        return ans
