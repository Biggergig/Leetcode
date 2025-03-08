class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k>len(s): return 0
        ans = 0
        chars = {c:0 for c in s}
        for c in range(k):
            chars[s[c]]+=1
        for i in range(k,len(s)):
            if all(v<=1 for v in chars.values()):
                ans+=1
                print(chars)
            chars[s[i]]+=1
            chars[s[i-k]]-=1
        if all(v<=1 for v in chars.values()):
            ans+=1
            print(chars)
        return ans