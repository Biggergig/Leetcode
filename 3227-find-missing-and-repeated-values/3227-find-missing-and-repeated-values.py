class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        missing = set(range(1,len(grid)**2 + 1))
        dup = None
        for row in grid:
            for v in row:
                if v in missing:
                    missing.remove(v)
                else:
                    dup = v

        return [dup]+list(missing)