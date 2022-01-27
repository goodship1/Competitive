from collections import Counter
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        h1 = Counter(word1)
        h2 = Counter(word2)#
        h1.subtract(h2)
        for x in h1.values():
            if abs(x) >3:
                return False
        return True
        
