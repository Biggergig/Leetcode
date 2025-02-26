class Solution:
    def compress(self, chars: List[str]) -> int:
        s = 0
        last = None
        count=0
        for i,c in enumerate(chars):
            if c == last:
                count+=1
            else:
                if last is not None:
                    chars[s] = last
                    s+=1
                    if count>1:
                        for digit in str(count):
                            chars[s] = digit
                            s+=1
                last = c
                count = 1
        if last is not None:
            chars[s] = last
            s+=1
            if count>1:
                for digit in str(count):
                    chars[s] = digit
                    s+=1
        return s