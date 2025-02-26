# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptr = [headA, headB]
        while ptr[0] != ptr[1]:
            for i in range(2):
                ptr[i] = [headB,headA][i] if ptr[i] is None else ptr[i].next
        return ptr[0]

        # length = [0,0]
        # for i,head in enumerate([headA,headB]):
        #     while head:
        #         length[i]+=1
        #         head = head.next
        # for _ in range(max(length[0]-length[1], 0)):
        #     headA = headA.next
        # for _ in range(max(length[1]-length[0], 0)):
        #     headB = headB.next
        # while headA:
        #     if headA == headB:
        #         return headA
        #     headA = headA.next
        #     headB = headB.next