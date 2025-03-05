class Solution:
    def minSwaps(self, data: List[int]) -> int:
        win_size = sum(data)
        best = cur = sum(data[:win_size])
        for i in range(win_size, len(data)):
            cur += data[i] - data[i-win_size]
            if cur>best:
                best=cur
        return win_size-best