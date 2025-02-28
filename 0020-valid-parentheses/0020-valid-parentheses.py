class Solution:
    def isValid(self, s: str) -> bool:
        S = []
        mapping = dict(zip("})]", "{(["))
        for c in s:
            if c in mapping:
                if S == [] or S[-1] != mapping[c]:
                    return False
                S.pop()
            else:
                S.append(c)
        return S == []
            

            