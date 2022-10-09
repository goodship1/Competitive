class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        store_1 = []
        store_2  = []
        for path in paths:
            store_1.append(path[0])
            store_2.append(path[1])
        for x in store_2:
            if x not in store_1:
                return x

