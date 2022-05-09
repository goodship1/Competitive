class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums.count(target)>0:
            left   = bisect.bisect_left(nums,target)
            right = bisect.bisect_right(nums,target)
            return [left,right-1]
        else:
            return [-1,-1]
        
