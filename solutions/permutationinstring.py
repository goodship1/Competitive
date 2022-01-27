from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        for i in range(len(s2)-len(s1)+1):
            if Counter(s2[i:i+len(s1)]) == counter: return True
        return False
        
        
