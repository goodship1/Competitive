class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        result = ''
        b = []
        for x in A:
            result +=str(x)
        strint = int(result)+K
        for x in str(strint):
            b.append(x)
        return b
        
