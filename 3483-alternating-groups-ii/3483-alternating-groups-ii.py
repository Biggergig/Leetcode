class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        valid_w_next = [a!=b for a,b in zip(colors, colors[1:] + colors[:1])]
        k-=1 # don't check if end value is needed
        ans = 0
        window = sum(valid_w_next[:k])
        pos = 0
        while pos != len(colors):
            window += valid_w_next[(pos+k)%len(valid_w_next)]-valid_w_next[pos]
            ans+=window==k
            pos+=1

        return ans