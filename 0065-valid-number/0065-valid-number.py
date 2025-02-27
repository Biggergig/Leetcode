import re
class Solution:
    def isNumber(self, s: str) -> bool:
        return re.fullmatch(r"[+-]?((\d*\.?\d+)|(\d+\.?\d*))([eE][+-]?\d+)?",s) is not None

    def isNumber(self, s: str) -> bool:
        try:
            if "n" in s: return False
            float(s)
            return True
        except:
            return False