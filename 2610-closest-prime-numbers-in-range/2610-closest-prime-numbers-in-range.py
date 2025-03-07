class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(n):
            if n<2: return False
            for div in range(2, int(n**.5)+1):
                if n%div == 0:
                    return False
            return True
        best=inf
        bestPair = [-1,-1]
        a=b=None
        for n in range(left, right+1):
            if isPrime(n):
                a,b=b,n
                if a is not None:
                    if b-a < best:
                        bestPair = [a,b]
                        best = b-a
                        if best == 2:
                            return bestPair
        return bestPair