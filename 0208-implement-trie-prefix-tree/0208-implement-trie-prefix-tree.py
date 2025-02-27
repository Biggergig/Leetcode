from collections import defaultdict
class Trie:
    def __init__(self):
        self.M = defaultdict(Trie)
        self.end = False

    def insert(self, word: str) -> None:
        if word:
            self.M[word[0]].insert(word[1:])
        else:
            self.end = True

    def search(self, word: str) -> bool:
        if not word:
            return self.end
        if word[0] not in self.M:
            return False
        return self.M[word[0]].search(word[1:])
        

    def startsWith(self, word: str) -> bool:
        if not word:
            return True
        if word[0] not in self.M:
            return False
        return self.M[word[0]].startsWith(word[1:])


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)