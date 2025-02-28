from bisect import bisect
class SnapshotArray:

    def __init__(self, length: int):
        self.snapshots = [[] for _ in range(length)]
        self.snap_num = 0

    def set(self, index: int, val: int) -> None:
        while self.snapshots[index] and self.snapshots[index][-1][0] == self.snap_num:
            self.snapshots[index].pop() # remove redundant values
        self.snapshots[index].append((self.snap_num, val))

    def snap(self) -> int:
        self.snap_num += 1
        return self.snap_num - 1        

    def get(self, index: int, snap_id: int) -> int:
        ind_snapshots = self.snapshots[index]
        ind = bisect_left(ind_snapshots, (snap_id+1,))-1
        if ind < 0: return 0
        return ind_snapshots[ind][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)