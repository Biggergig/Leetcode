from heapq import *
class MedianFinder:

    def __init__(self):
        self.lh = [] # store values as negatives
        self.rh = []

    def addNum(self, num: int) -> None:
        # push to whatever side of median it should be
        if (not self.lh and not self.rh) or num < self.findMedian():
            heappush(self.lh, -num)
        else:
            heappush(self.rh, num)

        while len(self.lh)-1>len(self.rh):
            heappush(self.rh, -heappop(self.lh))
        while len(self.rh)-1>len(self.lh):
            heappush(self.lh, -heappop(self.rh))
        

    def findMedian(self) -> float:
        if len(self.lh)>len(self.rh):
            return -self.lh[0]
        if len(self.rh)>len(self.lh):
            return self.rh[0]
        return (-self.lh[0] + self.rh[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()