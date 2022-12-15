class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for x in range(0,len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x]==nums[y] and (x*y)%k ==0:
                    count+=1
        return count
