from collections import Counter
class Trie:
    def __init__(self):
        infdict = lambda: defaultdict(infdict)
        self.T = infdict()
    def add(self, word):
        t = self.T
        for c in word:
            t = t[c]
        t['#'] = True
    def remove(self, word):
        t = self.T
        for c in word:
            if c not in t: return
            t = t[c]
        del t['#']
    def gen(self):
        def helper(path,t):
            if '#' in t:
                yield path
            for c in sorted(t.keys()):
                if c == '#': continue
                yield from helper(path+c, t[c])
        yield from helper("",self.T)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        C = Counter(words)
        k_most_common = C.most_common()
        k_most_common.sort(key=lambda x: (-x[1],x[0]))
        return [s for s,_ in k_most_common[:k]]
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        C = Counter(words)
        buckets = [Trie() for _ in range(len(words)+1)]
        for w,f in C.items():
            buckets[f].add(w)
        out = []
        for bi in range(len(buckets)-1,-1,-1):
            out+=buckets[bi].gen()
            if len(out)>=k:
                return out[:k]