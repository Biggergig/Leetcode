class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": return 0
        seen = set(s[0])
        l,r=0,1
        ans = 1
        while r<len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            r+=1
            if r-l > ans:
                ans = r-l
        return ans