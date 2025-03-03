from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bins = defaultdict(list)
        for s in strs:
            bins["".join(sorted(s))].append(s)
        return list(bins.values())