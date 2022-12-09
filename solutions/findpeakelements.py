class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for x in range(len(nums)-1):
            if nums[x+1] < nums[x]:
                return x
        return len(nums)-1

        
