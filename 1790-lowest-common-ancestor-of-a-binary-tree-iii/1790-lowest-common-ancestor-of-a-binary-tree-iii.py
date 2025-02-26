"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        heights = [0,0]
        for i in range(2):
            t = (p,q)[i]
            while t:
                heights[i]+=1
                t = t.parent
        while heights[0] > heights[1]:
            heights[0]-=1
            p = p.parent
        while heights[1] > heights[0]:
            heights[1]-=1
            q = q.parent
        while q.val != p.val:
            q = q.parent
            p = p.parent
        return q