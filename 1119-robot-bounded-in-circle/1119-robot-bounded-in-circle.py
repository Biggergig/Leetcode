class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = 0
        d = -1j
        for _ in range(4):
            for i in instructions:
                if i == "G":
                    pos+=d
                elif i == "L":
                    d*=1j
                elif i == "R":
                    d*=-1j
            if d == -1j:
                return pos == 0
