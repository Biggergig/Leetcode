class Solution:
    def closestFair(self, n: int) -> int:
        def fair(n):
            if n == 0: return 1
            s = 0
            while n:
                s+=-1 if (n%2) else 1
                n//=10
            return s
        while fair(n):
            n+=1
            if len(str(n))%2: # odd length, we NEED to start at next largest 10^n
                n = 10**(len(str(n)))
        return n
        print(fair(n))