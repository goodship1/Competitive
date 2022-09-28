class Solution:
    def countTriples(self, n: int) -> int:
        count  = 0
        for x in range(1,n):
            for y in range(x+1,n):
                check = math.sqrt(x*x+y*y)
                if int(check) == check and check <= n:
                    count+=2
        return count
