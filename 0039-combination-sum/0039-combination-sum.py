class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        def dfs(path, s, i):
            if s >= target:
                if s == target:
                    out.append(path[:])
                return
            if i == len(candidates):
                return
            dfs(path, s, i+1)
            path.append(candidates[i])
            dfs(path, s+candidates[i], i)
            path.pop()
        dfs([],0,0)
        return out