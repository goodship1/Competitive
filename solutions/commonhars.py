class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c = collections.Counter(words[0])
        for x in words:
            c &= collections.Counter(x)
        return list(c.elements())
