from collections import deque
class Solution:
    def compressedString(self, word: str) -> str:
        q = deque(word+"#") # sentinel value
        last = None
        count = 0
        out = ""
        while q:
            v = q.popleft()
            if v == last and count < 9:
                count+=1
            else:
                if count:
                    out+=f"{count}{last}"
                count = 1
                last = v
        return out