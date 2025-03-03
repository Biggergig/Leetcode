# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        best = 0
        def getZigLengths(n):
            # return left, right
            nonlocal best
            if n is None: return -1,-1
            left_zig = 1 + getZigLengths(n.left)[1]
            right_zig = 1 + getZigLengths(n.right)[0]
            best = max(best, left_zig, right_zig)
            return left_zig, right_zig
        getZigLengths(root)
        return best