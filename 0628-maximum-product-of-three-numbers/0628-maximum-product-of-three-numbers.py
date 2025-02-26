class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        combos = [
            (0,1,-1),
            (-1,-2,-3),
            (0,-1,-2)
        ]
        return max([nums[a]*nums[b]*nums[c] for a,b,c in combos])