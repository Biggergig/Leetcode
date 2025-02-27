from operator import add,sub,mul,floordiv
class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
    def __str__(self):
        n = self
        out = "<"
        while n is not None:
            out+=f" {n.val} "
            n = n.next
        out+=">"
        return out
    def calculate(self):
        assert self.val in "*/+-"
        ops = {
            "*":mul,
            "/":floordiv,
            "+":add,
            "-":sub
        }
        lhs = self.prev.val
        rhs = self.next.val
        self.val = ops[self.val](lhs, rhs)
        self.prev.prev.next = self
        self.next.next.prev = self
        self.prev = self.prev.prev
        self.next = self.next.next

class Solution:
    # Linked list solution
    def calculate(self, s: str) -> int:
        tok = list(s)
        operators = "*/+-"
        muldiv = []
        addsub = []
        for i in range(len(tok)-1,0,-1):
            if tok[i] not in operators and tok[i-1] not in operators:
                # both digits, so combine
                tok[i-1]+=tok[i]
                del tok[i] # fine apparently, doesn't matter about resized iterator!
        for i in range(len(tok)):
            if tok[i] not in operators:
                tok[i] = int(tok[i])
        head = Node("START")
        tail = Node("END",prev=head)
        head.next = tail
        for t in tok:
            tail.val = t
            if type(t) != int:
                if t in "*/":
                    muldiv.append(tail)
                else:
                    addsub.append(tail)
            tail.next = Node("END", tail)
            tail = tail.next
        for n in muldiv+addsub:
            n.calculate()
        return head.next.val
    
    # Stack solution
    def calculate(self, s: str) -> int:
        S = []
        curNum = ""
        lastOp = "+"
        op=None
        for c in s+"+": # sentinel value
            if c in " ": continue # skip whitespace
            if c in "0123456789":
                curNum+=c
            else:
                lastOp,op = op,c
                curNum = int(curNum)
                if lastOp == "*":
                    curNum=S.pop()*curNum
                if lastOp == "/":
                    curNum=int(S.pop()/curNum)
                while len(S)>=2: # this makes it constant space
                    S[0] += S.pop()
                S.append(curNum)
                curNum = "" if op != '-' else "-"
                if op == '-':op = "+"

        return sum(S)