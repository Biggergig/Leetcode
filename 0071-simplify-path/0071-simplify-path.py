class Solution:
    def simplifyPath(self, path: str) -> str:
        out = []
        for tok in path.split('/'):
            if not tok: continue # ignore //+
            if tok == '.': continue
            if tok == '..':
                if out: out.pop()
            else:
                out.append(tok)
        return "/"+"/".join(out)