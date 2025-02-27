import re
class Solution:
    def isNumber(self, s: str) -> bool:
        return re.fullmatch(r"[+-]?((\d*\.?\d+)|(\d+\.?\d*))([eE][+-]?\d+)?",s) is not None