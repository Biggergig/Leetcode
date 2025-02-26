from functools import cache
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # Just to not worry about duplicate calls
        @cache
        def get(i):return mountainArr.get(i)

        l,r=0,mountainArr.length()-1
        while l<r:
            m = (l+r)//2
            incr = get(m) < get(m+1)
            if incr:
                l = m+1
            else:
                r = m
        peak = l
        def search(l,r):
            print("searching",l,r)
            if l>=r: return l if get(l) == target else -1
            if get(l) == target:return l
            if get(r) == target:return r
            bounds = [get(l),get(r)]
            if not min(bounds)<=target<=max(bounds): return -1
            m = (l+r)//2
            if get(m) == target: return m
            lbounds = [get(l), get(m)]
            if min(lbounds)<=target<=max(lbounds): return search(l, m-1)
            return search(m+1,r)
        v = search(0,peak)
        if v!=-1: return v
        return search(peak, mountainArr.length()-1)