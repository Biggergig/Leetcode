from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        C = Counter(s)
        if min(C.values())>1: return -1
        for i,c in enumerate(s):
            if C[c] == 1: return i
