class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        x = [sum(nums)]
        res = []
        for x in range(len(nums)):
            for y in range(x,len(nums)):
                    s = sum(nums[x:y+1])
                    res.append(s)
            if len(res) == len(nums):
                break

        return res
