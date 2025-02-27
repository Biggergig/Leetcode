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
    
    # Below is wrong, since it skips a potentially shorter but better sequence

    # can we just keep track of deltas? - no because its not subarray but subsequence
    def WRONG_lenLongestFibSubseq(self, arr: List[int]) -> int:
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
