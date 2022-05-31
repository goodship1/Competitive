class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        if len(nums) <=2:
            return nums
        odd = []
        even = []
        for x,y in enumerate(nums):
            if x%2==0:
                even.append(y)
            else:
                odd.append(y)
        even = sorted(even)
        odd =  sorted(odd,reverse=True)
        res = []
        while even or odd:
            if even:
                res.append(even.pop(0))
            if odd:
                res.append(odd.pop(0))
        return res
                
        
