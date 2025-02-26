from math import comb
from collections import *
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        C = Counter(nums)
        freq = [*C.values()]
        ans=l=0
        r=len(nums)
        # Since we're doing a nested loop and summing it up, instead just keep a 
        # running total of values to left and right to multiply with
        for f in freq:
            r -= f
            ans += l * f * r
            l += f
        return ans

        # for i in range(len(freq)):
        #     for j in range(i+1,len(freq)):
        #         for k in range(j+1,len(freq)):
        #             ans += freq[i]*freq[j]*freq[k]
        # return ans
        # ans = 0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if nums[i]!=nums[j]!=nums[k]!=nums[i]: # python trick since nested ands
        #                 ans+=1
        # return ans