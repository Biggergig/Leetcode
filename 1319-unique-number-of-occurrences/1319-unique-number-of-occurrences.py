from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        C = Counter(arr)
        counts = C.values()
        return len(set(counts)) == len(counts)
