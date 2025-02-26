class Fenwick:
    def __init__(self, n):
        self.arr = [0]*(n+1)
        # 1 indexed
    def mark(self, i):
        i+=1
        while i<len(self.arr):
            self.arr[i]+=1
            i+=i&-i
    def query(self, i):
        i+=1
        out = 0
        while i:
            out+=self.arr[i]
            i-=i&-i
        return out
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        mn = min(nums)
        nums = [n-mn for n in nums]
        F = Fenwick(max(nums)+1)
        out = [0]*len(nums)
        for i,n in enumerate(reversed(nums)):
            out[-i-1] = F.query(n-1)
            F.mark(n)
        return out
