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

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes = [headA, headB]
        depths = [0,0]
        for i in range(2):
            while nodes[i] is not None:
                nodes[i] = nodes[i].next
                depths[i]+=1
        nodes = [headA, headB]
        for _ in range(depths[1],depths[0]):
            nodes[0] = nodes[0].next
        for _ in range(depths[0],depths[1]):
            nodes[1] = nodes[1].next
        while nodes[0] != nodes[1]:
            nodes[0] = nodes[0].next
            nodes[1] = nodes[1].next
        return nodes[0]
