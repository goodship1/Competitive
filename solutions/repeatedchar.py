class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = []
        for x in s:
            if x not in seen:
                seen.append(x)
            else:
                return x
        
