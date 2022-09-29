class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        rev = []
        for x in s:
            if x !='':
                rev.append(x)
        return ' '.join(reversed(rev))
