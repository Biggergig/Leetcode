class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []

        def helper(path, l, r):
            # path = current string
            # l = how many left parenthesis I have to place
            # r = how many right parenthesis I have to place
            if l == 0 and r == 0:
                out.append(path)
                return
            if l > 0:
                helper(path+"(", l-1, r)
            if l<r: # more open parenthesis than closing ones
                helper(path+")", l, r-1)

        helper("", n, n)
        return out