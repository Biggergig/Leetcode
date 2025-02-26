from itertools import accumulate
class Fenwick:
    def __init__(self, size):
        self.L = [0]*(size+1)
    def mark(self, i):
        i+=1
        while i<len(self.L):
            self.L[i]+=1
            i += i&-i
    def query(self, i):
        i+=1
        out=0
        while i:
            out+=self.L[i]
            i -= i&-i
        return out
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        local_inversions = sum([a>b for a,b in zip(nums,nums[1:])])

        F = Fenwick(len(nums))
        global_inversions = 0
        for n in reversed(nums):
            global_inversions += F.query(n)
            F.mark(n)
        print(local_inversions, global_inversions)
        return global_inversions == local_inversions

    def isIdealPermutation(self, nums: List[int]) -> bool:
        # every local inversion is a global inversion, so we just
        # want to search for any non-local inversions and return False

        # We can find this out by checking if n[i] > n[i+2, i+3, ...]
        # this is the same as n[i] > min(n[i+2:])
        # same thing as n[i] < max(n[:i-2])

        # don't need this since we can just keep running total
        # prefix_max = list(accumulate(nums,max))
        mx = nums[0]
        for i,n in enumerate(nums[:-2]): # skip last 2
            mx = max(mx, n)
            if nums[i+2] < mx: return False
        return True
    
    def isIdealPermutation(self, nums: List[int]) -> bool:
        # For all permutations with that pass, a number cannot be swapped more than 
        # 1 away from it's source location

        # think about 1 2 3 4 5
        # if I shift 3 to either
        #             V   or  V
        # think about 1 2   4 5
        # we need to replace it with a value larger than it, otherwise non-local inversion
        # we now need to have all values from that point onwards larger than this val, and
        # so we have to fill n slots with larger numbers but we only have n-1 larger numbers

        for i,n in enumerate(nums):
            if abs(n-i) > 1: return False
        return True
    
    def isIdealPermutation(self, nums: List[int]) -> bool:
        # More pythonic

        return all(abs(n-i)<=1 for i,n in enumerate(nums))
