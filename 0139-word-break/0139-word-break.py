from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def canSolve(i)->bool:
            # true if the rest of the string is valid
            if i == len(s): return True
            for w in wordDict:
                if s[i:i+len(w)] == w and canSolve(i+len(w)):
                    return True
            return False
        return canSolve(0)