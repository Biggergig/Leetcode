class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

    def reverseWords(self, s: str) -> str:
        s = list(s.strip())
        
        l=0
        def rev(a,b):
            while a<b:
                s[a],s[b] = s[b],s[a]
                a+=1
                b-=1
                
        for r in range(len(s)+1):
            if r==len(s) or s[r] == ' ':
                if r>0 and s[r-1] == ' ':
                    s[r-1] = ''
                rev(l,r-1)
                l=r+1
        rev(0,len(s)-1)

        return "".join(s)