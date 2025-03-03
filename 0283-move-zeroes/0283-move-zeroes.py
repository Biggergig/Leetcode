class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r,v in enumerate(nums):
            if v:
                nums[r] = 0
                nums[l] = v
                l+=1
        