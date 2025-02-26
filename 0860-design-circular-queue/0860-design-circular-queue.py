class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None]*k
        self.f = self.r = 0
        self.open_spaces = k
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.open_spaces == 0: return False
        self.q[self.r] = value
        self.r = (self.r+1)%self.k
        self.open_spaces -= 1
        return True
        

    def deQueue(self) -> bool:
        if self.open_spaces == self.k: return False
        value = self.q[self.f]
        self.f = (self.f+1)%self.k
        self.open_spaces += 1
        return True
        

    def Front(self) -> int:
        if self.open_spaces == self.k: return -1
        return self.q[self.f]
        

    def Rear(self) -> int:
        if self.open_spaces == self.k: return -1
        return self.q[(self.r - 1)%self.k]
        

    def isEmpty(self) -> bool:
        return self.open_spaces == self.k
        

    def isFull(self) -> bool:
        return self.open_spaces ==0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()