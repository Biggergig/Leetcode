from collections import Counter
from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums): return nums
        C = Counter(nums)
        H = []
        for n,f in C.items():
            heappush(H,(f,n))
            if len(H)>k:
                heappop(H)
        return [n for f,n in H]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        C = Counter(nums)
        return nlargest(k, C.keys(), key=C.get)

    # Quick select
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        C = Counter(nums)
        un = list(C)
        def quickSelect(l,r): # non-inclusive range
            if l == r-1: return un[l:]
            pivot = un[l]
            pivotCount = C[pivot]
            slow = l
            i = l+1
            end = r-1
            while i<=end:
                if C[un[i]] < pivotCount:
                    un[slow] = un[i]
                    slow = i
                    i+=1
                else:
                    # swap with right side, but stay on this i
                    un[i],un[end] = un[end],un[i]
                    end-=1
            un[slow] = pivot
            if len(un)-slow == k:
                return un[slow:]
            if len(un)-slow < k:
                return quickSelect(l,slow)
            return quickSelect(slow+1,r)
        return quickSelect(0,len(un))