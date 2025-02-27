class Solution:
    def decodeString(self, s: str) -> str:
        nums = []
        strs = [""]
        curNum = 0
        for c in s:
            if c.isnumeric():
                curNum = curNum*10 + int(c)
            elif c == '[':
                strs.append("")
                nums.append(curNum)
                curNum = 0
            elif c == ']':
                curStr = strs.pop()
                n = nums.pop()
                strs[-1]+=curStr*n
            else:
                strs[-1]+=c
        return strs[0]