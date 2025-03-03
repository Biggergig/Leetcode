from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def flatten(it):
            if type(it) == list:
                for v in it:
                    yield from flatten(v)
            else:
                yield it
        def isValid(it):
            C = Counter(flatten(it))
            for k,v in C.items():
                if k == '.': continue
                if v>1: return False
            return True

        for row in board:
            if not isValid(row): return False
        for x in range(len(board[0])):
            if not isValid([r[x] for r in board]): return False
        for y in range(3):
            for x in range(3):
                if not isValid([r[3*x:3*(x+1)] for r in board[y*3:(y+1)*3]]): return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows,cols,boxes = ([set() for _ in range(9)] for _ in range(3))

        for y,row in enumerate(board):
            for x,val in enumerate(row):
                if val == '.': continue
                for bin in (rows[y], cols[x], boxes[y//3 + 3 * (x//3)]):
                    if val in bin: return False
                    bin.add(val)
        return True