from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        C1 = Counter(word1)
        C2 = Counter(word2)
        if C1.keys() != C2.keys(): return False # they have different letters
        for (_,fa),(_,fb) in zip(C1.most_common(), C2.most_common()):
            if fa!=fb: return False # different frequency maps
        return True