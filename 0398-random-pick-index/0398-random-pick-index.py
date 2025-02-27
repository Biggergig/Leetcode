from random import choice
from collections import defaultdict
class Solution:

    def __init__(self, nums: List[int]):
        self.inds = defaultdict(list)
        for i,n in enumerate(nums):
            self.inds[n].append(i)

    def pick(self, target: int) -> int:
        return choice(self.inds[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)