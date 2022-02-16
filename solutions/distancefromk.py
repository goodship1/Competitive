class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        distance = k
        for n in nums:
            if n == 0:
                distance += 1
            elif n == 1 and distance < k:
                return False
            else:
                distance = 0
        return True

