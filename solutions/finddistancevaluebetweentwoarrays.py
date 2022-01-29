class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = len(arr1)
        for x in arr1:
            for y in arr2:
                if abs(x -y)>d:
                    continue
                else:
                    count-=1
                    break
        return count
