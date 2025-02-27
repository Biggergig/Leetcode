# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def __init__(self):
    #     self.cache = {}
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     lhs = sum([self.hasV(root.left, v) for v in (p,q)])
    #     rhs = sum([self.hasV(root.right, v) for v in (p,q)])
    #     print(lhs, rhs)
    #     if lhs == 1 or rhs == 1:
    #         return root
    #     if lhs == 2:
    #         return self.lowestCommonAncestor(root.left, p, q)
    #     return self.lowestCommonAncestor(root.right, p, q)
    # def hasV(self, node, v):
    #     if (node, v) in self.cache:
    #         return self.cache[(node,v)]
    #     if not node: return 0
    #     if node.val == v.val: 
    #         self.cache[node, v] = 1
    #         return 1
    #     self.cache[node, v] = int(self.hasV(node.left, v) or self.hasV(node.right, v))
    #     return self.cache[node,v]
    

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {}
        depths = {}
        def helper(n, parent=None, depth=0):
            if n is None: return
            parents[n] = parent
            if n in (p,q):
                depths[n] = depth
            helper(n.left, n, depth+1)
            helper(n.right, n, depth+1)
        helper(root)
        for _ in range(-min(depths.values()) + depths[p]):
            p = parents[p]
        for _ in range(-min(depths.values()) + depths[q]):
            q = parents[q]
        while p!=q:
            p = parents[p]
            q = parents[q]
        return p
