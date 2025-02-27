from random import *
class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.mapping = {}
        self.size = n - len(blacklist)
        r=n-1
        # move blacklist elements to end of array "swapping" them, then sample only from remaining
        blacklist = set(blacklist)
        for l in blacklist:
            if l>=self.size: continue # if it's already in the end portion we can skip it
            while r in blacklist:
                r-=1
            self.mapping[l] = r
            r-=1
        print(self.mapping)
    def pick(self) -> int:
        i = randrange(self.size)
        return self.mapping.get(i,i)


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()