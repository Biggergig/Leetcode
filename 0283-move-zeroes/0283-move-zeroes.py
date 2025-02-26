class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[s] = nums[i]
                s+=1
        for j in range(s,len(nums)):
            nums[j] = 0

