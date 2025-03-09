from collections import defaultdict
class Node:
    def __init__(self, val):
        self.val=val
        self.par=None
        self.edges = []
        self.bob_time = inf
    def getVal(self, time):
        if time < self.bob_time:
            return self.val
        if time == self.bob_time:
            return self.val / 2
        else:
            return 0
    def addEdge(self, edge):
        self.edges.append(edge)
        # edge.par = self
    def setParents(self):
        self.edges = [e for e in self.edges if e.par is None] # if already processed, then its higher than this
        for e in self.edges:
            e.par = self
        for e in self.edges:
            e.setParents()
    def __repr__(self):
        return f"<({self.val}) t:{self.bob_time}>"# - [{len(self.edges)} children]>"

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        nodes = {i:Node(v) for i,v in enumerate(amount)}
        for a,b in edges:
            nodes[a].addEdge(nodes[b])
            nodes[b].addEdge(nodes[a])
        nodes[0].par = "TMP"
        nodes[0].setParents()
        nodes[0].par = None
        t = 0
        n = nodes[bob]
        while n:
            n.bob_time = t
            n = n.par
            t += 1
        def mostProfit(n, t, profit):
            profit += n.getVal(t)
            if len(n.edges) == 0:
                return profit # is leaf node
            return max(mostProfit(child, t+1, profit) for child in n.edges)
        return int(mostProfit(nodes[0], 0, 0))