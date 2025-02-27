from collections import defaultdict
class Trie:
    def __init__(self):
        infdict = lambda: defaultdict(infdict)
        self.T = infdict()
    def insert(self, word: str) -> None:
        t = self.T
        for c in word:
            t=t[c]
        t['#'] = True # Marking character        
    def search(self, word: str) -> bool:
        t = self.T
        for c in word:
            if c not in t: return False
            t=t[c]
        return '#' in t
    def startsWith(self, word: str) -> bool:
        t = self.T
        for c in word:
            if c not in t: return False
            t=t[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)