class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff = arr[1] - arr[0]
        for x in range(len(arr)-1):
            if (arr[x+1] - arr[x])<diff:
                diff = arr[x+1] -arr[x]
        res = []
        for x in range(len(arr)-1):
            if arr[x] < arr[x+1] and arr[x+1] - arr[x] == diff:
                res.append([arr[x],arr[x+1]])
        return res
