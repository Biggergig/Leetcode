class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i<len(s) and s[i] == ' ':
            i+=1
        pos = True
        if i<len(s) and s[i] in "+-":
            pos = s[i] == "+"
            i+=1
        val = 0
        while i<len(s) and '0'<=s[i]<='9':
            val = val*10 + ord(s[i])-ord('0')
            i+=1
        return max(min(val*(1 if pos else -1), 2**31-1), -(2**31))
