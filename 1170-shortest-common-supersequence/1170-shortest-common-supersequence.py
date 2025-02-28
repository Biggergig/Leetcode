class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        prevRow = [""]
        for c in str1:
            prevRow.append(prevRow[-1]+c)
        for c2 in str2:
            nextRow = prevRow[:]
            nextRow[0]+=c2
            for i1, c1 in enumerate(str1):
                if c1 == c2:
                    nextRow[i1+1] = prevRow[i1]+c2
                else:
                    nextRow[i1+1] = min(prevRow[i1+1]+c2, nextRow[i1]+c1, key=len)
            prevRow = nextRow
        return nextRow[-1]