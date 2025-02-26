# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        length = [0,0]
        for i,head in enumerate([headA,headB]):
            while head:
                length[i]+=1
                head = head.next
        for _ in range(max(length[0]-length[1], 0)):
            headA = headA.next
        for _ in range(max(length[1]-length[0], 0)):
            headB = headB.next
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
