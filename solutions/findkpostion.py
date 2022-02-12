class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        for x in range(1,len(arr)+k+1):
            if x not in arr:
                count+=1
                if count == k:
                    return x 
        
