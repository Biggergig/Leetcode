from math import log
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        base = int(log(n,3))+1
        while n:
            if 3**base <= n:
                n -= 3**base
                if n>=3**base: return False
            base-=1
        return n == 0