from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def hash(w):
            out = [0]*26
            for c in w:
                out[ord(c)-ord('a')]+=1
            return tuple(out)
        bins = defaultdict(list)
        for w in strs:
            bins[hash(w)].append(w)
        return list(bins.values())