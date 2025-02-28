"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, n: Optional['Node']) -> Optional['Node']:
        if n is None: return None
        cache = {}
        def dfs(cur):
            # Returns the deepcopied node
            if cur in cache:
                return cache[cur]
            copied_node = Node(cur.val)
            cache[cur] = copied_node
            copied_node.neighbors =  [dfs(e) for e in cur.neighbors]
            return copied_node
        return dfs(n)
