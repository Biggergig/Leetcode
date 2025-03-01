class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i,v in enumerate(nums):
            if i+1<len(nums) and v == nums[i+1]:
                nums[i]*= 2
                nums[i+1] = 0
        slow = 0
        for v in nums:
            if v:
                nums[slow] = v
                slow+=1
        while slow<len(nums):
            nums[slow] = 0
            slow+=1
        return nums