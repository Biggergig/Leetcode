class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        for i,n in enumerate(nums):
            if i+1 == len(nums) or nums[i+1] != n:
                nums[l] = n
                l+=1
        return l