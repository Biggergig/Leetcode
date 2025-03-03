class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniques = {}
        seen = set()
        for i,c in enumerate(s):
            if c in uniques:
                seen.add(c)
                del uniques[c]
            elif c not in seen:
                uniques[c] = i
        if uniques:
            return min(uniques.values())
        return -1