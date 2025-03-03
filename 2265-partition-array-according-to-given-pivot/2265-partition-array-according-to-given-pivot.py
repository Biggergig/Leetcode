class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = [n for n in nums if n<pivot]
        larger = [n for n in nums if n>pivot]
        pivots = [pivot]*(len(nums)-len(smaller)-len(larger))
        return smaller+pivots+larger