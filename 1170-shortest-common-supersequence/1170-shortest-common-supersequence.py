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

    # don't store string explicitly, but rather supersequence length
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        DP = [[inf]*(len(str1)+1) for _ in range(len(str2)+1)]
        for y in range(len(DP)): DP[y][0] = y
        for x in range(len(DP[0])): DP[0][x] = x

        for y in range(1, len(DP)):
            for x in range(1, len(DP[0])):
                if str1[x-1] == str2[y-1]:
                    DP[y][x] = DP[y-1][x-1]+1
                else:
                    DP[y][x] = min(DP[y-1][x],DP[y][x-1])+1
                
        out = []
        x,y=len(DP[0])-1,len(DP)-1
        while x or y:
            print(x,y)
            if x and DP[y][x-1] == DP[y][x]-1:
                x-=1
                out+=str1[x]
            elif y and DP[y-1][x] == DP[y][x]-1:
                y-=1
                out+=str2[y]
            else:
                y-=1
                x-=1
                out+=str2[y]
        return "".join(reversed(out))