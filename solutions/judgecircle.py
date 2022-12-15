class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        first  = moves.count("U")==moves.count("D") 
        second = moves.count("R") == moves.count("L")
        return first and second
