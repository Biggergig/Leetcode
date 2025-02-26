from math import comb
from collections import *
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        C = Counter(nums)
        freq = [*C.values()]
        print(freq)
        ans = 0
        for i in range(len(freq)):
            for j in range(i+1,len(freq)):
                for k in range(j+1,len(freq)):
                    ans += freq[i]*freq[j]*freq[k]
        return ans
        # ans = 0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if nums[i]!=nums[j]!=nums[k]!=nums[i]: # python trick since nested ands
        #                 ans+=1
        # return ans