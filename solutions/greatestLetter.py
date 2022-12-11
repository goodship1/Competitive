class Solution:
    def greatestLetter(self, s: str) -> str:
        upper  = []
        lower = []
        store = []
        for x in range(len(s)):
            if s[x].isupper():
                upper.append(s[x])
            else:
                lower.append(s[x])
        upper = sorted(upper)
        lower = sorted(lower)
        for x in range(len(lower)):
            if lower[x].upper() in upper:
                store.append(lower[x].upper())
        if len(store)==0:
            return ""
        else:
            return max(store)
        e
