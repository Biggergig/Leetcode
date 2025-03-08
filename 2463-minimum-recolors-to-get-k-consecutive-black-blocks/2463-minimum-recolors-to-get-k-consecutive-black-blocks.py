class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        best = k
        for i in range(len(blocks)-k+1):
            best = min(best, blocks[i:i+k].count("W"))
        return best
            