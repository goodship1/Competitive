class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        store = []
        for x in matrix:
            for y in x:
                store.append(y)
        if target in store:
            return True
        else:
            return False
        
