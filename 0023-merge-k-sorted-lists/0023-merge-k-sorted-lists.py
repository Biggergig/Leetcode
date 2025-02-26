from heapq import *
class Node:
    def __init__(self, n):
        self.n = n
    def __lt__(self, other):
        return self.n.val < other.n.val
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = [Node(n) for n in lists if n]
        heapify(h)
        dummy = ListNode()
        tail = dummy

        while h:
            tmp = heappop(h)
            # print("list:",dummy.next)
            # print(tmp)
            tail.next = tmp.n
            tail = tail.next
            if tail.next:
                heappush(h, Node(tail.next))
            tail.next = None

        return dummy.next