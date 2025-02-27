"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None: return None # base case
        # with our inorder traversal, after we process a node we don't need it's children again
        # so then it's safe to rewrite

        def make_dll(n)->list[Node|None]:
            # base case
            if n.left is None and n.right is None:
                return [n,n] # return this as both the start and end of the list
            
            # Incase one of the children is invalid, since we are returning these just return n
            lh=rt=n

            # handle left
            if n.left is not None: # only if we had a left node
                lh,lt = make_dll(n.left) # get left head and left tail
                lt.right = n
                n.left = lt
            # handle this node

            # handle right
            if n.right is not None: # only if we had a right node
                rh, rt = make_dll(n.right) # get right head and right tail
                rh.left = n
                n.right = rh
            
            return [lh, rt]
        head, tail = make_dll(root)
        head.left = tail
        tail.right = head
        # while h:
        #     print(f"<{h.val}>", end =" ")
        #     h = h.right
        # print()
        return head