from bisect import bisect_left
from collections import deque
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l=r=bisect_left(arr, x)
        l-=1
        print(l,r)
        out = deque()
        for _ in range(k):
            if r>=len(arr) or (l>=0 and abs(arr[l]-x) <= abs(arr[r]-x)):
                out.appendleft(arr[l])
                l-=1
            else:
                out.append(arr[r])
                r+=1

        return list(out)