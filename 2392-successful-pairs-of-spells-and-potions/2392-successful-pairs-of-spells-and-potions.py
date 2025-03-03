class Fenwick:
    def __init__(self, arr):
        self.mn = min(arr)
        mn = min(arr)
        mx = max(arr)
        self.T = [0]*(mx-mn+2)
        for v in arr:
            self.T[v-mn+1]+=1
        for i in range(1, len(self.T)):
            par = i + (i&-i)
            if par < len(self.T):
                self.T[par]+=self.T[i]
    def valsLarger(self, val):
        def query(i):
            if i>=len(self.T):
                i = len(self.T)-1
            out = 0
            while 0<i:
                out+=self.T[i]
                i-=(i&-i)
            return out
        i = (val-self.mn) # not doing +1 since want smaller value than current
        return query(len(self.T)-1) - query(i)

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        F = Fenwick(potions)
        return [F.valsLarger(math.ceil(success/spell)) for spell in spells]
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        return [len(potions)-bisect.bisect_left(potions, success/s) for s in spells]
