class Solution:
    def isValid(self, s: str) -> bool:
        pairings = dict(zip(")}]","({["))
        S = []
        for c in s:
            if c in pairings:
                if not S or S[-1] != pairings[c]: return False
                S.pop()
            else:
                S.append(c)
        return not S