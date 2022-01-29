class Solution:
    def trimMean(self, arr: List[int]) -> float:
        new_array =  sorted(arr)
        five_percent =  int(len(arr)*0.05)
        n  = len(arr)
        new_array  = new_array[five_percent:n-five_percent]
        return sum(new_array)/len(new_array)a
