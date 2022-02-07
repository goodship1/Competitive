from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        result = ""
        c = Counter(list(s)).most_common()
        #c.sort()
        for x in c:
            result = result+x[0]*x[1]
        return result
