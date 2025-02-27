from random import *
class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.mapping = {}
        self.size = n - len(blacklist)
        r=n-1
        blacklist = set(blacklist)
        for l in blacklist:
            while r in blacklist:
                r-=1
            if l>r: break
            self.mapping[l] = r
            r-=1
        print(self.mapping)
    def pick(self) -> int:
        i = randrange(self.size)
        return self.mapping.get(i,i)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()