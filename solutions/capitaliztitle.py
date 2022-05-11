class Solution:
    def capitalizeTitle(self, title: str) -> str:
        s = title.split()
        result = []
        for x in s:
            if len(x) <3:
                result.append(x.lower())
            else:
                result.append(x.capitalize())
        return ' '.join(result)          
