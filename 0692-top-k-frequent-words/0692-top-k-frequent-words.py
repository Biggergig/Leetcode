from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        C = Counter(words)
        k_most_common = C.most_common()
        k_most_common.sort(key=lambda x: (-x[1],x[0]))
        return [s for s,_ in k_most_common[:k]]