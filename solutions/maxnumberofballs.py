class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ball = collections.defaultdict(int)
        for x in range(lowLimit,highLimit+1):
            s = str(x)
            if len(s) == 1:
                ball[x] = 1
            if len(s) >=2:
                balls  = sum([int(y) for y in s])
                ball[balls] = ball[balls] + 1
        return max(ball.values())
            
        
