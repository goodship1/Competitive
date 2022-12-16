class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = 0
        l =  len(nums)
        for x in nums:
            if nums.count(x) % 2 == 0:
                count+=1
        if count == l:
            return True
        return False
