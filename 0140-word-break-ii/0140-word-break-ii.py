class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        out = []
    
        def helper(path, suffix):
            # path is list of words already split
            # suffix is the rest of the string
            if suffix == "":
                out.append(" ".join(path))
                return
            for w in wordDict:
                if suffix.startswith(w):
                    helper(path+[w], suffix[len(w):])
        helper([], s)
        return out