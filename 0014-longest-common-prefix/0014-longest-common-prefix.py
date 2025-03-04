from collections import defaultdict
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        infdict = lambda: defaultdict(infdict)
        T=infdict()
        for w in strs:
            t = T
            for c in w:
                t = t[c]
                t['count']=t.get('count',0)+1
        req_count = len(strs)
        def helper(t):
            for k,v in t.items():
                if k == "count": continue
                if v.get('count',0) == req_count:
                    return k+helper(v)
            return ""
        return helper(T)

    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        for chars in zip(*strs):
            if len(set(chars)) != 1: break
            pre+=chars[0]
        return pre
