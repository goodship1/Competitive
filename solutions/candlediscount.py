class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        s = sorted(cost,reverse=True)
        price = 0
        for x in range(0,len(cost)):
            if (x +1)%3 ==0:
                continue
            else:
                price +=s[x]
        return price
                https://www.google.com/search?client=ubuntu&channel=fs&q=githubcom&ie=utf-8&oe=utf-8
