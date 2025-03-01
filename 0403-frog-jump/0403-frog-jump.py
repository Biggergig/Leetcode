class Solution:
    def canCross(self, stones: List[int]) -> bool:
        target = stones[-1]
        positions = set(stones)

        seen = set()
        def helper(i, k):
            if (i, k) in seen: return False
            seen.add((i, k))

            if i == target:
                return True
            for jump in (k + 1, k, k - 1):
                if jump == 0: continue
                if jump + i in positions:
                    if helper(i + jump, jump):
                        return True
            return False

        if stones[1] != 1: return False
        return helper(1, 1)