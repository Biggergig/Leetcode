class Solution:
    def longestValidParentheses(self, s: str) -> int:
        best = 0
        S = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                S.append(i)
            else:
                S.pop()
                if not S:
                    S.append(i) # restart stack
                else:
                    best = max(best, i-S[-1])
        return best
