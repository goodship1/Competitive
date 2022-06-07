class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_in_row = [min(x) for x in matrix]
        for index in range(len(matrix[0])):
            column_max = max([x[index] for x in matrix])
            if column_max in min_in_row:
                return [column_max]
