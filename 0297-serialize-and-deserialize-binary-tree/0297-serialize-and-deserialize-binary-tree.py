# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None: return ""
        return f"{root.val}[{self.serialize(root.left)}][{self.serialize(root.right)}]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return
        def unpack(i):
            if data[i] == ']': return None, i+1
            val = ""
            while data[i].isnumeric() or data[i] == '-':
                val+=data[i]
                i+=1
            n = TreeNode(int(val))
            n.left,i = unpack(i+1)
            n.right,i = unpack(i+1)
            return n,i+1
        return unpack(0)[0]

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))