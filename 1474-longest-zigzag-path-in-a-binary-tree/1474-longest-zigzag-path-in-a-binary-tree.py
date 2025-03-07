# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def helper(n, l, r):
            nonlocal ans
            if n is None:
                ans=max(ans, l, r)
                return
            helper(n.left, r+1, 0)
            helper(n.right, 0, l+1)
        helper(root,0,0)
        return ans-1