from collections import defaultdict
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        nums = set(arr)
        best = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                a,b = arr[i],arr[j]
                l = 2
                while a+b in nums:
                    a,b = b,a+b
                    l+=1
                if l > 2:  # This single line speeds up a ton of time??
                    best = max(best, l)
        return best if best >=3 else 0


    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # This is with DP - the idea being DP[x][x1] = len
        # where x1 is a prev value and the length from that sequence
        DP = defaultdict(lambda: defaultdict(int))
        nums = set(arr)
        seen = set()
        for n in arr:
            for x1 in seen:
                if n+x1 in nums: # this line is necessary for time!
                    DP[n+x1][n] = max(DP[n+x1][n], 2)
            for x1, l in DP[n].items():
                DP[n+x1][n] = max(DP[n+x1][n], l+1)
            seen.add(n)
        v = max([max(D.values()) for D in DP.values() if D]+[0])
        return v if v>=3 else 0

    
    # Below is wrong, since it skips a potentially shorter but better sequence - needs to be 2d

    def WRONG_lenLongestFibSubseq(self, arr: List[int]) -> int:
        # can we just keep track of deltas? - no because its not subarray but subsequence
        # key is the value we are looking for, values = [len, x_-1]
        tails = defaultdict(lambda: (-inf,inf)) # default to a value that is always smaller than any other tuple
        seen = set() # measure singletons to start sequences
        upper_bound = arr[-1]
        best = 0
        for n in arr:
            for v in seen:
                if n+v <= upper_bound:
                    print("starter for",v+n,":",tails[v+n], end='\t')
                    tails[n+v] = max(tails[n+v],(2, n, v))
                    print(tails[v+n])
                    # print("Starting sequence",tails[n+v],"at",n+v)
            if n in tails:
                l, x1, *rem = tails[n]
                print("Can continue sequence", tails[n], "with",n)
                print(tails[x1+n], end='\t')
                tails[x1+n] = (l+1, n, x1, *rem)
                print(tails[x1+n])
                best=max(best, l+1)
            seen.add(n)
        return best if best >= 3 else 0
